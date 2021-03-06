# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class MachineExtensionOperations(object):
    """MachineExtensionOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~connected_machine.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def _create_or_update_initial(
        self,
        resource_group_name,  # type: str
        name,  # type: str
        extension_name,  # type: str
        location,  # type: str
        tags=None,  # type: Optional[Dict[str, str]]
        force_update_tag=None,  # type: Optional[str]
        publisher=None,  # type: Optional[str]
        type_properties_type=None,  # type: Optional[str]
        type_handler_version=None,  # type: Optional[str]
        auto_upgrade_minor_version=None,  # type: Optional[bool]
        settings=None,  # type: Optional[object]
        protected_settings=None,  # type: Optional[object]
        status=None,  # type: Optional["models.MachineExtensionInstanceViewStatus"]
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["models.MachineExtension"]
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["models.MachineExtension"]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        extension_parameters = models.MachineExtension(tags=tags, location=location, force_update_tag=force_update_tag, publisher=publisher, type_properties_type=type_properties_type, type_handler_version_properties_type_handler_version=type_handler_version, auto_upgrade_minor_version=auto_upgrade_minor_version, settings=settings, protected_settings=protected_settings, status=status)
        api_version = "2020-08-02"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._create_or_update_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'name': self._serialize.url("name", name, 'str'),
            'extensionName': self._serialize.url("extension_name", extension_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(extension_parameters, 'MachineExtension')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('MachineExtension', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    _create_or_update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/machines/{name}/extensions/{extensionName}'}  # type: ignore

    def begin_create_or_update(
        self,
        resource_group_name,  # type: str
        name,  # type: str
        extension_name,  # type: str
        location,  # type: str
        tags=None,  # type: Optional[Dict[str, str]]
        force_update_tag=None,  # type: Optional[str]
        publisher=None,  # type: Optional[str]
        type_properties_type=None,  # type: Optional[str]
        type_handler_version=None,  # type: Optional[str]
        auto_upgrade_minor_version=None,  # type: Optional[bool]
        settings=None,  # type: Optional[object]
        protected_settings=None,  # type: Optional[object]
        status=None,  # type: Optional["models.MachineExtensionInstanceViewStatus"]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["models.MachineExtension"]
        """The operation to create or update the extension.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param name: The name of the machine where the extension should be created or updated.
        :type name: str
        :param extension_name: The name of the machine extension.
        :type extension_name: str
        :param location: The geo-location where the resource lives.
        :type location: str
        :param tags: Resource tags.
        :type tags: dict[str, str]
        :param force_update_tag: How the extension handler should be forced to update even if the
         extension configuration has not changed.
        :type force_update_tag: str
        :param publisher: The name of the extension handler publisher.
        :type publisher: str
        :param type_properties_type: Specifies the type of the extension; an example is
         "CustomScriptExtension".
        :type type_properties_type: str
        :param type_handler_version: Specifies the version of the script handler.
        :type type_handler_version: str
        :param auto_upgrade_minor_version: Indicates whether the extension should use a newer minor
         version if one is available at deployment time. Once deployed, however, the extension will not
         upgrade minor versions unless redeployed, even with this property set to true.
        :type auto_upgrade_minor_version: bool
        :param settings: Json formatted public settings for the extension.
        :type settings: object
        :param protected_settings: The extension can contain either protectedSettings or
         protectedSettingsFromKeyVault or no protected settings at all.
        :type protected_settings: object
        :param status: Instance view status.
        :type status: ~connected_machine.models.MachineExtensionInstanceViewStatus
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either MachineExtension or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~connected_machine.models.MachineExtension]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MachineExtension"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._create_or_update_initial(
                resource_group_name=resource_group_name,
                name=name,
                extension_name=extension_name,
                location=location,
                tags=tags,
                force_update_tag=force_update_tag,
                publisher=publisher,
                type_properties_type=type_properties_type,
                type_handler_version=type_handler_version,
                auto_upgrade_minor_version=auto_upgrade_minor_version,
                settings=settings,
                protected_settings=protected_settings,
                status=status,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('MachineExtension', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/machines/{name}/extensions/{extensionName}'}  # type: ignore

    def _update_initial(
        self,
        resource_group_name,  # type: str
        name,  # type: str
        extension_name,  # type: str
        tags=None,  # type: Optional[Dict[str, str]]
        force_update_tag=None,  # type: Optional[str]
        publisher=None,  # type: Optional[str]
        type=None,  # type: Optional[str]
        type_handler_version=None,  # type: Optional[str]
        auto_upgrade_minor_version=None,  # type: Optional[bool]
        settings=None,  # type: Optional[object]
        protected_settings=None,  # type: Optional[object]
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["models.MachineExtension"]
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["models.MachineExtension"]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        extension_parameters = models.MachineExtensionUpdate(tags=tags, force_update_tag=force_update_tag, publisher=publisher, type=type, type_handler_version=type_handler_version, auto_upgrade_minor_version=auto_upgrade_minor_version, settings=settings, protected_settings=protected_settings)
        api_version = "2020-08-02"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._update_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'name': self._serialize.url("name", name, 'str'),
            'extensionName': self._serialize.url("extension_name", extension_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(extension_parameters, 'MachineExtensionUpdate')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('MachineExtension', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    _update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/machines/{name}/extensions/{extensionName}'}  # type: ignore

    def begin_update(
        self,
        resource_group_name,  # type: str
        name,  # type: str
        extension_name,  # type: str
        tags=None,  # type: Optional[Dict[str, str]]
        force_update_tag=None,  # type: Optional[str]
        publisher=None,  # type: Optional[str]
        type=None,  # type: Optional[str]
        type_handler_version=None,  # type: Optional[str]
        auto_upgrade_minor_version=None,  # type: Optional[bool]
        settings=None,  # type: Optional[object]
        protected_settings=None,  # type: Optional[object]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["models.MachineExtension"]
        """The operation to update the extension.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param name: The name of the machine where the extension should be created or updated.
        :type name: str
        :param extension_name: The name of the machine extension.
        :type extension_name: str
        :param tags: Resource tags.
        :type tags: dict[str, str]
        :param force_update_tag: How the extension handler should be forced to update even if the
         extension configuration has not changed.
        :type force_update_tag: str
        :param publisher: The name of the extension handler publisher.
        :type publisher: str
        :param type: Specifies the type of the extension; an example is "CustomScriptExtension".
        :type type: str
        :param type_handler_version: Specifies the version of the script handler.
        :type type_handler_version: str
        :param auto_upgrade_minor_version: Indicates whether the extension should use a newer minor
         version if one is available at deployment time. Once deployed, however, the extension will not
         upgrade minor versions unless redeployed, even with this property set to true.
        :type auto_upgrade_minor_version: bool
        :param settings: Json formatted public settings for the extension.
        :type settings: object
        :param protected_settings: The extension can contain either protectedSettings or
         protectedSettingsFromKeyVault or no protected settings at all.
        :type protected_settings: object
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either MachineExtension or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~connected_machine.models.MachineExtension]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MachineExtension"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._update_initial(
                resource_group_name=resource_group_name,
                name=name,
                extension_name=extension_name,
                tags=tags,
                force_update_tag=force_update_tag,
                publisher=publisher,
                type=type,
                type_handler_version=type_handler_version,
                auto_upgrade_minor_version=auto_upgrade_minor_version,
                settings=settings,
                protected_settings=protected_settings,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('MachineExtension', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/machines/{name}/extensions/{extensionName}'}  # type: ignore

    def _delete_initial(
        self,
        resource_group_name,  # type: str
        name,  # type: str
        extension_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-08-02"

        # Construct URL
        url = self._delete_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'name': self._serialize.url("name", name, 'str'),
            'extensionName': self._serialize.url("extension_name", extension_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/machines/{name}/extensions/{extensionName}'}  # type: ignore

    def begin_delete(
        self,
        resource_group_name,  # type: str
        name,  # type: str
        extension_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller[None]
        """The operation to delete the extension.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param name: The name of the machine where the extension should be deleted.
        :type name: str
        :param extension_name: The name of the machine extension.
        :type extension_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._delete_initial(
                resource_group_name=resource_group_name,
                name=name,
                extension_name=extension_name,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/machines/{name}/extensions/{extensionName}'}  # type: ignore

    def get(
        self,
        resource_group_name,  # type: str
        name,  # type: str
        extension_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MachineExtension"
        """The operation to get the extension.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param name: The name of the machine containing the extension.
        :type name: str
        :param extension_name: The name of the machine extension.
        :type extension_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MachineExtension, or the result of cls(response)
        :rtype: ~connected_machine.models.MachineExtension
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MachineExtension"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-08-02"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'name': self._serialize.url("name", name, 'str'),
            'extensionName': self._serialize.url("extension_name", extension_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MachineExtension', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/machines/{name}/extensions/{extensionName}'}  # type: ignore

    def list(
        self,
        resource_group_name,  # type: str
        name,  # type: str
        expand=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.MachineExtensionsListResult"]
        """The operation to get all extensions of a non-Azure machine.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param name: The name of the machine containing the extension.
        :type name: str
        :param expand: The expand expression to apply on the operation.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either MachineExtensionsListResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~connected_machine.models.MachineExtensionsListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MachineExtensionsListResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-08-02"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'name': self._serialize.url("name", name, 'str'),
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if expand is not None:
                    query_parameters['$expand'] = self._serialize.query("expand", expand, 'str')
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('MachineExtensionsListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/machines/{name}/extensions'}  # type: ignore
