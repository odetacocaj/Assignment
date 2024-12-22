from flask import Blueprint, jsonify, request
from db.query_data import get_all_characters, search_characters, get_character_by_id

main = Blueprint('main', __name__)


@main.route('/api/characters', methods=['GET'])
def get_characters():
    query = request.args.get('search')  

   
    if query:
        if len(query.strip()) == 0:
            return jsonify({"message": "Search query is too short."}), 400 
        characters = search_characters(query)  
    else:
        characters = get_all_characters()  

    return jsonify(characters)  



@main.route('/api/characters/<int:character_id>', methods=['GET'])
def get_single_character(character_id):
    character = get_character_by_id(character_id)
    
    if character:
        return jsonify(character)  
    else:
        return jsonify({"message": "Character not found"}), 404  
