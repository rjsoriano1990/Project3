

var dropdownMenu = d3.select("#Dates");
var date = dropdownMenu.property("value");




d3.json(`/gas1/${date}`).then(data=>{
    console.log(data)
});

function DateChanged2(date)  {

d3.json(`/gas1/${date}`).then(data=>{
  console.log(data)
});
}


function DateChanged(date)  {

  d3.json(`/gas1/${date}`).then(data=>{
    console.log(data)
  })
  }

// dropdown for regions
var dropdownMenu = d3.select("#Region");
var region = dropdownMenu.property("value");
    
    
    
    
  d3.json(`/gas2/${region}`).then(data=>{
      console.log(data)
  })
    
function DateChanged2(region)  {
    
  d3.json(`/gas2/${region}`).then(data=>{
      console.log(data)
  })
  }
    
    
function DateChanged(date)  {
    
  d3.json(`/gas2/${date}`).then(data=>{
      console.log(data)
  })
  };