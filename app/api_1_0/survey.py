# Copyright (C) 2016 University of Zurich.  All rights reserved.
#
# This file is part of MSRegistry Backend.
#
# MSRegistry Backend is free software: you can redistribute it and/or
# modify it under the terms of the version 3 of the GNU Affero General
# Public License as published by the Free Software Foundation, or any
# other later version.
#
# MSRegistry Backend is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the version
# 3 of the GNU Affero General Public License for more details.
#
# You should have received a copy of the version 3 of the GNU Affero
# General Public License along with MSRegistry Backend.  If not, see 
# <http://www.gnu.org/licenses/>.

__author__ = "Filippo Panessa <filippo.panessa@uzh.ch>"
__copyright__ = ("Copyright (c) 2016 S3IT, Zentrale Informatik,"
" University of Zurich")


from flask import jsonify, request, _request_ctx_stack

from . import api
from app.models.role import Role
from app.models.survey import Survey

from app.auth.decorators import requires_auth, requires_roles, requires_consent

from werkzeug.exceptions import BadRequest


@api.route('/survey', methods=['GET'])
@requires_auth
def get_survey():
    survey = Survey()
    return jsonify(surveys=[ob.serialize() for ob in survey.getAllByUniqueID(_request_ctx_stack.top.uniqueID)])


@api.route('/survey', methods=['POST'])
@requires_auth
@requires_roles(roles=[Role.patient, Role.relative])
@requires_consent
def add_survey():
    survey = Survey()
    content = request.get_json(silent=True)
    if content:
        return jsonify(success=bool(survey.addByUniqueID(_request_ctx_stack.top.uniqueID, content)))
    
    return jsonify(success=bool(False))


@api.route('/survey/<string:_id>', methods=['GET'])
@requires_auth
@requires_roles(roles=[Role.patient, Role.relative])
def get_survey_by_id(_id):
    survey = Survey()
    result = survey.getByUniqueIDAndID(_request_ctx_stack.top.uniqueID, _id)
    if result is not None:
        return jsonify(result.serialize())
    
    raise BadRequest('Survey not found', status_code=404, 
                            payload={'code': 'not_found'})


