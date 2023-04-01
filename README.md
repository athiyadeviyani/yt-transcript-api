# yt-transcript-api

Usage in javascript file
```
function get_transcript(video_id) {
    var joke = "";
    return fetch("https://yt-transcript-api.herokuapp.com/?video="+video_id, {
        headers: {
            Accept: "application/json"
        },
        method: 'GET',
    }).then(resp => {
        return resp.json()
    }).then(r => {
        console.log(r.MESSAGE);

    })

}

const video_ID = 'aKVvdgfbmWw'
get_transcript(video_ID)
```
