function loadStatistics (pk, githubUrl, downUrl) {
    document.getElementById(`${pk}-refresh`).disabled = true;
    const GURL = githubUrl;
    const DOWN = downUrl;
    
    const downloadStats = () => {
        const downStatsOptions = {
            url: DOWN,
            responseType: 'json',
            success: (payload) => {
                const downDis = document.getElementById(`down-${pk}`);
                if (downDis) {
                    downDis.innerText = payload.response.hasOwnProperty('downloads')? payload.response.downloads: 0;
                };
            },
            error: () => {}
        }

        ajax.get(downStatsOptions);
    };
    
    if (GURL !== 'None') {
        const fills = {
            PULL_REQUESTS: 'pulls',
            COMMITS: 'commits',
            ISSUES: 'issues',
            FORKS: 'forks',
            STARS: 'stars'
        };
    
        /**
        * @param {fills}  fillType
        * @param {number}  pk_
        * @param {number}  value
        * @returns {void}
        */
        const fillDetails = (pk_, fillType, value) => document.getElementById(`${fillType}-${pk_}`).innerText = value;
    
        const processCommits = (payload) => payload.map((load) => load.total).reduce((acc, item) => acc + item);
    
        const options = {
            url: GURL,
            responseType: 'json',
            success: (response) => {
                const load = response.response;
                const stats = [
                    [load.hasOwnProperty('open_issues_count')? load.open_issues_count: 0, fills.ISSUES],
                    [load.hasOwnProperty('forks_count')? load.forks_count: 0, fills.FORKS],
                    [load.hasOwnProperty('stargazers_count')? load.stargazers_count: 0, fills.STARS]
                ]
                stats.forEach(([val, type_]) => fillDetails(pk, type_, val));
    
                if (load.hasOwnProperty('pulls_url')) {
                    const pullsOptions = {
                        url: load.pulls_url.replace(/\{\/\w+\}$/g, ''),
                        responseType: 'json',
                        success: (response) => {
                            const pulls_ = Array.isArray(response.response)? response.response.length: 0;
                            fillDetails(pk, fills.PULL_REQUESTS, pulls_);
    
                            if (load.hasOwnProperty('commits_url')) {
                                const commitsOptions = {
                                    url: `${GURL}/stats/contributors`,
                                    responseType: 'json',
                                    success: (response) => {
                                        const commits_ = Array.isArray(response.response)? processCommits(response.response): 0;
                                        fillDetails(pk, fills.COMMITS, commits_);

                                        if (DOWN !== 'None') {
                                            downloadStats();
                                        };
                                    },
                                    error: () => {}
                                };
                
                                ajax.get(commitsOptions);
                            };
    
                        },
                        error: () => {}
                    };
    
                    ajax.get(pullsOptions);
                };
            },
            error: () => {}
        };
    
        ajax.get(options);

    } else if (DOWN !== 'None') {
        downloadStats();
    };
};