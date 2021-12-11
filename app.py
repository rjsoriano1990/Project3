from flask import Flask,render_template, jsonify, request
from sqlalchemy import create_engine
from config import post_pass
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

# create and modify the flask app
app = Flask(__name__)

# engine and connect to sql DB
connection_string = f"postgres:{post_pass}@localhost:5432/Project3"
engine = create_engine(f'postgresql://{connection_string}')

Base = automap_base()
Base.prepare(engine, reflect=True)


# save references to table 
#set table variable
us_gas_prices_region = Base.classes.us_gas_prices_region

# opening standard route
@app.route('/')
def home():
    with open ('templates/project3.html') as f:
        return f.read()

@app.route('/gas1/<date>')
def date_func(date):

    # map
    session = Session(engine)
    results = session.query(us_gas_prices_region.date, us_gas_prices_region.east_coast, us_gas_prices_region.new_england, 
                            us_gas_prices_region.central_atlantic, us_gas_prices_region.lower_atlantic, us_gas_prices_region.midwest,
                            us_gas_prices_region.gulf_coast, us_gas_prices_region.rocky_mountains, us_gas_prices_region.west_coast).filter(us_gas_prices_region.date == date).all()
    session.close()



    map = []
    for date,  east_coast, new_england, central_atlantic, lower_atlantic, midwest, gulf_coast, rocky_mountains, west_coast in results:
        results_dic = {}
        results_dic['date'] = date
        results_dic[ "east_coast"] =  east_coast
        results_dic["new_england"] = new_england
        results_dic['central_atlantic'] = central_atlantic
        results_dic['lower_atlantic'] = lower_atlantic
        results_dic['midwest'] = midwest
        results_dic['gulf_coast'] = gulf_coast
        results_dic['rocky_mountains'] = rocky_mountains
        results_dic['west_coast'] = west_coast
            
        map.append(results_dic)
        
    #results
    return jsonify(map)

####

@app.route('/gas2/<east_coast>')
def east_coast_func(east_coast):

    # map
    session = Session(engine)
    results = session.query(us_gas_prices_region.date, us_gas_prices_region.east_coast, us_gas_prices_region.new_england, 
                            us_gas_prices_region.central_atlantic, us_gas_prices_region.lower_atlantic, us_gas_prices_region.midwest,
                            us_gas_prices_region.gulf_coast, us_gas_prices_region.rocky_mountains, us_gas_prices_region.west_coast).filter(us_gas_prices_region.east_coast == east_coast).all()
    session.close()

    viz_1 = []
    for date, east_coast in results:
        results_dic = {}
        results_dic['date'] = date
        results_dic['east_coast'] = east_coast
        viz_1.append(results_dic)
    return jsonify(viz_1 )

####

@app.route('/gas2/<new_england>')
def new_england_func(new_england):

    # map
    session = Session(engine)
    results = session.query(us_gas_prices_region.date, us_gas_prices_region.east_coast, us_gas_prices_region.new_england, 
                            us_gas_prices_region.central_atlantic, us_gas_prices_region.lower_atlantic, us_gas_prices_region.midwest,
                            us_gas_prices_region.gulf_coast, us_gas_prices_region.rocky_mountains, us_gas_prices_region.west_coast).filter(us_gas_prices_region.new_england == new_england).all()
    session.close()

    viz_2 = []
    for date, new_england in results:
        results_dic = {}
        results_dic['date'] = date
        results_dic['new_england'] = new_england
        viz_2.append(results_dic)
        return jsonify(viz_2)

####

@app.route('/gas2/< central_atlantic>')
def  central_atlantic_func( central_atlantic):

    # map
    session = Session(engine)
    results = session.query(us_gas_prices_region.date, us_gas_prices_region.east_coast, us_gas_prices_region.new_england, 
                            us_gas_prices_region.central_atlantic, us_gas_prices_region.lower_atlantic, us_gas_prices_region.midwest,
                            us_gas_prices_region.gulf_coast, us_gas_prices_region.rocky_mountains, us_gas_prices_region.west_coast).filter(us_gas_prices_region.central_atlantic==  central_atlantic).all()
    session.close()
    viz_3 = []
    for date, central_atlantic in results:
        results_dic = {}
        results_dic['date'] = date
        results_dic['central_atlantic'] = central_atlantic
        viz_3.append(results_dic)
        return jsonify(viz_3) 


####

@app.route('/gas2/<lower_atlantic>')
def  lower_atlantic_func(lower_atlantic):

    # map
    session = Session(engine)
    results = session.query(us_gas_prices_region.date, us_gas_prices_region.east_coast, us_gas_prices_region.new_england, 
                            us_gas_prices_region.central_atlantic, us_gas_prices_region.lower_atlantic, us_gas_prices_region.midwest,
                            us_gas_prices_region.gulf_coast, us_gas_prices_region.rocky_mountains, us_gas_prices_region.west_coast).filter(us_gas_prices_region.lower_atlantic ==  lower_atlantic).all()
    session.close()
    viz_4 = []
    for date, lower_atlantic in results:
        results_dic = {}
        results_dic['date'] = date
        results_dic['lower_atlantic'] = lower_atlantic
        viz_4.append(results_dic)
        return jsonify(viz_4)

#####

@app.route('/gas2/<midwest>')
def  midwest_func(midwest):

    # map
    session = Session(engine)
    results = session.query(us_gas_prices_region.date, us_gas_prices_region.east_coast, us_gas_prices_region.new_england, 
                            us_gas_prices_region.central_atlantic, us_gas_prices_region.lower_atlantic, us_gas_prices_region.midwest,
                            us_gas_prices_region.gulf_coast, us_gas_prices_region.rocky_mountains, us_gas_prices_region.west_coast).filter(us_gas_prices_region.midwest ==  midwest).all()
    session.close()

    viz_5 = []
    for date, midwest in results:
        results_dic = {}
        results_dic['date'] = date
        results_dic['midwest'] = midwest
        viz_5.append(results_dic)
        return jsonify(viz_5) 

#####



@app.route('/gas2/<gulf_coast>')
def  gulf_coast_func(gulf_coast):

    # map
    session = Session(engine)
    results = session.query(us_gas_prices_region.date, us_gas_prices_region.east_coast, us_gas_prices_region.new_england, 
                            us_gas_prices_region.central_atlantic, us_gas_prices_region.lower_atlantic, us_gas_prices_region.midwest,
                            us_gas_prices_region.gulf_coast, us_gas_prices_region.rocky_mountains, us_gas_prices_region.west_coast).filter(us_gas_prices_region.gulf_coast ==  gulf_coast).all()
    session.close()

    viz_6 = []
    for date, gulf_coast in results:
        results_dic = {}
        results_dic['date'] = date
        results_dic['gulf_coast'] = gulf_coast
        viz_6.append(results_dic)
        return jsonify(viz_6)


######

@app.route('/gas2/<rocky_mountains>')
def  rocky_mountains_func(rocky_mountains):

    # map
    session = Session(engine)
    results = session.query(us_gas_prices_region.date, us_gas_prices_region.east_coast, us_gas_prices_region.new_england, 
                            us_gas_prices_region.central_atlantic, us_gas_prices_region.lower_atlantic, us_gas_prices_region.midwest,
                            us_gas_prices_region.gulf_coast, us_gas_prices_region.rocky_mountains, us_gas_prices_region.west_coast).filter(us_gas_prices_region.rocky_mountains ==  rocky_mountains).all()
    session.close()

    viz_7 = []
    for date, rocky_mountains in results:
        results_dic = {}
        results_dic['date'] = date
        results_dic['rocky_mountains'] = rocky_mountains
        viz_7.append(results_dic)
        return jsonify(viz_7)




@app.route('/gas2/<west_coast>')
def  west_coast_func(rocky_mountains):

    # map
    session = Session(engine)
    results = session.query(us_gas_prices_region.date, us_gas_prices_region.east_coast, us_gas_prices_region.new_england, 
                            us_gas_prices_region.central_atlantic, us_gas_prices_region.lower_atlantic, us_gas_prices_region.midwest,
                            us_gas_prices_region.gulf_coast, us_gas_prices_region.rocky_mountains, us_gas_prices_region.west_coast).filter(us_gas_prices_region.rocky_mountains ==  rocky_mountains).all()
    session.close()
    viz_8 = []
    for date, rocky_mountains in results:
        results_dic = {}
        results_dic['date'] = date
        results_dic['rocky_mountains'] = rocky_mountains
        viz_8.append(results_dic)
        return jsonify(viz_8)
       
    
    
    
      
    
    
    
    



"""
const activation_dropdown_id = '#selActivation'

// Attach the on-change-handler for the activation dropdown
d3.selectAll(activation_dropdown_id).on('change', updatePlot);

function updatePlot() {
  /*
   * This function updates the lineplot's data & title
   * with the values that are currently selected in the
   * #selActivation dropdown list.
   */

  // Get the selected dropdown's "value" attribute
  var activation = d3.select(activation_dropdown_id).property('value');
  // Get the selected dropdown's inner text. Note we add "option:checked" this time.
  var name = d3.select(`${activation_dropdown_id} option:checked`).text();

  // Build a href to get the activation data selected
  var dataUrl = `/data/${activation}?from=-5&to=5`;
  console.log(dataUrl);

  // Make a query to get the data, then update the graph 
  // with whatever data get's returned.
  d3.json(dataUrl).then(data => {
    let layout = {
      title: `This is a ${name} activation curve`
    };
    
    Plotly.newPlot("plot", [data], layout);
  });
}

// initialize graph
updatePlot();







    
"""

# extra ending thingy that I still dont understand 
if __name__ == '__main__':
    app.run(debug=True, port=8000)