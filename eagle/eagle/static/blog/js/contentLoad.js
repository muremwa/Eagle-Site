/* 
    Turn content to markdown
*/

[...document.getElementsByClassName('post-content')].forEach((container) => {
    const content = container.dataset.postContent;
    const markedContent = marked(content);
    container.innerHTML = markedContent;
})