from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/graph/health")
def health():
    return "Working fine"


@app.route("/api/graph/fields")
def fields():
    nodes_fields = [{"field_name": "id", "type": "string"},
                    {"field_name": "title", "type": "string",
                     },
                    {"field_name": "subTitle", "type": "string"},
                    {"field_name": "mainStat", "type": "string"},
                    {"field_name": "secondaryStat", "type": "number"},
                    {"field_name": "arc__frontend_candidate",
                     "type": "number", "color": "orange", "displayName":
                         "Frontend candidate"},
                    {"field_name": "arc__frontend_violator",
                     "type": "number", "color": "red", "displayName":
                         "Frontend violator"},
                    {"field_name": "detail__role",
                     "type": "string", "displayName": "Role"}]
    edges_fields = [
        {"field_name": "id", "type": "string"},
        {"field_name": "source", "type": "string"},
        {"field_name": "target", "type": "string"},
        {"field_name": "mainStat", "type": "number"},
    ]
    result = {"nodes_fields": nodes_fields,
              "edges_fields": edges_fields}
    return jsonify(result)
