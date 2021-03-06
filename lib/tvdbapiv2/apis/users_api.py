# coding: utf-8

"""
UsersApi.py
Copyright 2015 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class UsersApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def user_get(self, **kwargs):
        """

        Returns basic information about the currently authenticated user.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.user_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: UserData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/user'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client. \
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client. \
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwtToken']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='UserData',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def user_favorites_get(self, **kwargs):
        """

        Returns an array of favorite series for a given user, will be a blank array if no favorites exist.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.user_favorites_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: UserFavoritesData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_favorites_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/user/favorites'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client. \
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client. \
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwtToken']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='UserFavoritesData',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def user_favorites_id_put(self, id, **kwargs):
        """

        Adds the supplied series ID to the user’s favorite’s list and returns the updated list.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.user_favorites_id_put(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ID of the series (required)
        :return: UserFavoritesData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_favorites_id_put" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `user_favorites_id_put`")

        resource_path = '/user/favorites/{id}'.replace('{format}', 'json')
        method = 'PUT'

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client. \
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client. \
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwtToken']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='UserFavoritesData',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def user_favorites_id_delete(self, id, **kwargs):
        """

        Deletes the given series ID from the user’s favorite’s list and returns the updated list.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.user_favorites_id_delete(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: ID of the series (required)
        :return: UserFavoritesData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_favorites_id_delete" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `user_favorites_id_delete`")

        resource_path = '/user/favorites/{id}'.replace('{format}', 'json')
        method = 'DELETE'

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client. \
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client. \
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwtToken']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='UserFavoritesData',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def user_ratings_get(self, **kwargs):
        """

        Returns an array of ratings for the given user.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.user_ratings_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: UserRatingsData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_ratings_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/user/ratings'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client. \
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client. \
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwtToken']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='UserRatingsData',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def user_ratings_query_get(self, **kwargs):
        """

        Returns an array of ratings for a given user that match the query.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.user_ratings_query_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str item_type: Item to query. Can be either 'series', 'episode', or 'banner'
        :return: UserRatingsData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_type', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_ratings_query_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/user/ratings/query'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}
        if 'item_type' in params:
            query_params['itemType'] = params['item_type']

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client. \
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client. \
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwtToken']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='UserRatingsData',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def user_ratings_query_params_get(self, **kwargs):
        """

        Returns a list of query params for use in the `/user/ratings/query` route.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.user_ratings_query_params_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: UserRatingsQueryParams
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_ratings_query_params_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/user/ratings/query/params'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client. \
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client. \
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwtToken']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='UserRatingsQueryParams',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def user_ratings_item_type_item_id_delete(self, item_type, item_id, **kwargs):
        """

        This route deletes a given rating of a given type.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.user_ratings_item_type_item_id_delete(item_type, item_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str item_type: Item to update. Can be either 'series', 'episode', or 'image' (required)
        :param int item_id: ID of the ratings record that you wish to modify (required)
        :return: UserRatingsDataNoLinksEmptyArray
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_type', 'item_id', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_ratings_item_type_item_id_delete" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'item_type' is set
        if ('item_type' not in params) or (params['item_type'] is None):
            raise ValueError("Missing the required parameter `item_type` when calling `user_ratings_item_type_item_id_delete`")
        # verify the required parameter 'item_id' is set
        if ('item_id' not in params) or (params['item_id'] is None):
            raise ValueError("Missing the required parameter `item_id` when calling `user_ratings_item_type_item_id_delete`")

        resource_path = '/user/ratings/{itemType}/{itemId}'.replace('{format}', 'json')
        method = 'DELETE'

        path_params = {}
        if 'item_type' in params:
            path_params['itemType'] = params['item_type']
        if 'item_id' in params:
            path_params['itemId'] = params['item_id']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client. \
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client. \
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwtToken']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='UserRatingsDataNoLinksEmptyArray',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def user_ratings_item_type_item_id_item_rating_put(self, item_type, item_id, item_rating, **kwargs):
        """

        This route updates a given rating of a given type.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.user_ratings_item_type_item_id_item_rating_put(item_type, item_id, item_rating, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str item_type: Item to update. Can be either 'series', 'episode', or 'image' (required)
        :param int item_id: ID of the ratings record that you wish to modify (required)
        :param int item_rating: The updated rating number (required)
        :return: UserRatingsDataNoLinks
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_type', 'item_id', 'item_rating', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_ratings_item_type_item_id_item_rating_put" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'item_type' is set
        if ('item_type' not in params) or (params['item_type'] is None):
            raise ValueError("Missing the required parameter `item_type` when calling `user_ratings_item_type_item_id_item_rating_put`")
        # verify the required parameter 'item_id' is set
        if ('item_id' not in params) or (params['item_id'] is None):
            raise ValueError("Missing the required parameter `item_id` when calling `user_ratings_item_type_item_id_item_rating_put`")
        # verify the required parameter 'item_rating' is set
        if ('item_rating' not in params) or (params['item_rating'] is None):
            raise ValueError("Missing the required parameter `item_rating` when calling `user_ratings_item_type_item_id_item_rating_put`")

        resource_path = '/user/ratings/{itemType}/{itemId}/{itemRating}'.replace('{format}', 'json')
        method = 'PUT'

        path_params = {}
        if 'item_type' in params:
            path_params['itemType'] = params['item_type']
        if 'item_id' in params:
            path_params['itemId'] = params['item_id']
        if 'item_rating' in params:
            path_params['itemRating'] = params['item_rating']

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client. \
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client. \
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwtToken']

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='UserRatingsDataNoLinks',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
