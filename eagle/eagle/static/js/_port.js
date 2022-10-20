function loadStatistics (id, githubLink, statsLink) {
    if (githubLink && githubLink !== 'None') {
        // stars & forks
        fetch(`${githubLink}`, {
            method: 'GET'
        }).then((data) => data.json()).then((data) => {
            document.getElementById(`stars-${id}`).innerText = data['stargazers_count'];
            document.getElementById(`forks-${id}`).innerText = data['forks_count'];
        });

        // commits
        fetch(`${githubLink}/contributors?per_page=100`, {
            method: 'GET'
        }).then((data) => data.json()).then((data) => {
            const commits = document.getElementById(`commits-${id}`)
            commits.innerText = data.map((cont) => cont['contributions']).reduce((x, y) => x + y);
        });

        // pull requests & issues
        fetch(`${githubLink}/issues?per_page=100`, {
            method: 'GET'
        }).then((data) => data.json()).then((data) => {
            let issues = 0;
            let pulls = 0;

            data.forEach((issue) => {
                Object.keys(issue).includes('pull_request')? pulls++: issues++;
            });

            document.getElementById(`pulls-${id}`).innerText = pulls.toString();
            document.getElementById(`issues-${id}`).innerText = issues.toString();
        });
    }

    if (statsLink && statsLink !== 'None') {
        // download stats
        fetch(statsLink, {
            method: 'GET'
        }).then((data) => data.json()).then((data) => {
            document.getElementById(`down-${id}`).innerText = data['downloads'];
        });
    }
}


const observer = new IntersectionObserver((items) => {
    items.forEach((item) => {
        if (item.isIntersecting) {
            const element = item.target;
            const args = {...element.dataset};
            loadStatistics(args['id'], args['githubLink'], args['statsLink']);
            observer.unobserve(element)
        }
    });
}, {
    threshold: [0]
});

[...document.getElementsByClassName('stats-bar')].forEach((element) => {
    observer.observe(element);
});