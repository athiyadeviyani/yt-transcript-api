# yt-transcript-api

Usage in javascript file
```
function get_transcript(video_ID) {
    var joke = "";
    return fetch("https://yt-transcript-api.herokuapp.com/?video="+video_ID, {
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

get_transcript('aKVvdgfbmWw')
```
