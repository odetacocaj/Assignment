from flask import Blueprint, jsonify, request
from db.query_data import get_all_characters, search_characters, get_character_by_id

main = Blueprint('main', __name__)


@main.route('/api/characters', methods=['GET'])
def get_characters():
    query = request.args.get('search')  
    category = request.args.get('category')  

    if category and category not in ['vikings', 'norsemen']:
        return jsonify({"message": "Invalid category. Choose 'vikings' or 'norsemen'."}), 400

    if query:
        if len(query.strip()) == 0:
            return jsonify({"message": "Search query is too short."}), 400
        
        if category == 'vikings':
            characters = search_characters(query, category='vikings')
        elif category == 'norsemen':
            characters = search_characters(query, category='norsemen')
        else:
            characters = search_characters(query)  
    else:
        if category == 'vikings':
            characters = get_all_characters(category='vikings')
        elif category == 'norsemen':
            characters = get_all_characters(category='norsemen')
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
