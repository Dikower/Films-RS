let user_id = 2;
let back_url = "https://c1b9-176-213-135-3.ngrok.io/";
export async function getFilms(page: number){
  let path = back_url + "films?page="+page;
  const response = await fetch(
    path,
    {
      method: "GET",
      headers: { 
        Accept: "application/json;", 
        "Content-Type": "application/json",
      },
    }
  );
  if(response.ok === true){
    const out = await response.json()
    return(out);
  } else {
    console.log("ERROR in getFilms");
    const out = await response.json();
    console.log(out)
    return(out);
  } 
}
export async function getFilm(id: number){
  let path = back_url + "film/" + id;
  const response = await fetch(
    path,
    {
      method: "GET",
      headers: { 
        Accept: "application/json;", 
        "Content-Type": "application/json",
      },
    }
  );
  if(response.ok === true){
    const out = await response.json()
    return(out);
  } else {
    console.log("ERROR in getFilm");
    const out = await response.json();
    console.log(out)
    return(out);
  } 
}
export async function getMyFilms(){
  let path = back_url + "user_marks/" + user_id;
  const response = await fetch(
    path,
    {
      method: "GET",
      headers: { 
        Accept: "application/json;", 
        "Content-Type": "application/json",
      },
    }
  );
  if(response.ok === true){
    const out = await response.json()
    return(out);
  } else {
    console.log("ERROR in getMyFilms");
    const out = await response.json();
    console.log(out)
    return(out);
  }
}

export async function getSimilarFilms(movie_id: number){
  let path = back_url + "similar/" + movie_id;
  const response = await fetch(
    path,
    {
      method: "GET",
      headers: { 
        Accept: "application/json;", 
        "Content-Type": "application/json",
      },
    }
  );
  if(response.ok === true){
    const out = await response.json()
    return(out);
  } else {
    console.log("ERROR in getSimilarFilms");
    const out = await response.json();
    console.log(out)
    return(out);
  }
}

export async function getMyRecommendations(){
  let path = back_url + "top_recommendations/" + user_id;
  const response = await fetch(
    path,
    {
      method: "GET",
      headers: { 
        Accept: "application/json;", 
        "Content-Type": "application/json",
      },
    }
  );
  if(response.ok === true){
    const out = await response.json()
    return(out);
  } else {
    console.log("ERROR in getMyRecommendations");
    const out = await response.json();
    console.log(out)
    return(out);
  }
}