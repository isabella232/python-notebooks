# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple

from google.api_core import grpc_helpers_async  # type: ignore
from google.api_core import operations_v1  # type: ignore
from google.auth import credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore
from grpc.experimental import aio  # type: ignore

from google.cloud.notebooks_v1beta1.types import environment
from google.cloud.notebooks_v1beta1.types import instance
from google.cloud.notebooks_v1beta1.types import service
from google.longrunning import operations_pb2 as operations  # type: ignore

from .base import NotebookServiceTransport
from .grpc import NotebookServiceGrpcTransport


class NotebookServiceGrpcAsyncIOTransport(NotebookServiceTransport):
    """gRPC AsyncIO backend transport for NotebookService.

    API service for Cloud AI Platform Notebooks.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(
        cls,
        host: str = "notebooks.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            address (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """
        scopes = scopes or cls.AUTH_SCOPES
        return grpc_helpers_async.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            **kwargs,
        )

    def __init__(
        self,
        *,
        host: str = "notebooks.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: aio.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        quota_project_id=None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[aio.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): The mutual TLS endpoint. If
                provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]): A
                callback to provide client SSL certificate bytes and private key
                bytes, both in PEM format. It is ignored if ``api_mtls_endpoint``
                is None.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        if channel:
            # Sanity check: Ensure that channel and credentials are not both
            # provided.
            credentials = False

            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
        elif api_mtls_endpoint:
            host = (
                api_mtls_endpoint
                if ":" in api_mtls_endpoint
                else api_mtls_endpoint + ":443"
            )

            # Create SSL credentials with client_cert_source or application
            # default SSL credentials.
            if client_cert_source:
                cert, key = client_cert_source()
                ssl_credentials = grpc.ssl_channel_credentials(
                    certificate_chain=cert, private_key=key
                )
            else:
                ssl_credentials = SslCredentials().ssl_credentials

            # create a new channel. The provided one is ignored.
            self._grpc_channel = type(self).create_channel(
                host,
                credentials=credentials,
                credentials_file=credentials_file,
                ssl_credentials=ssl_credentials,
                scopes=scopes or self.AUTH_SCOPES,
                quota_project_id=quota_project_id,
            )

        # Run the base constructor.
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes or self.AUTH_SCOPES,
            quota_project_id=quota_project_id,
        )

        self._stubs = {}

    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Sanity check: Only create a new channel if we do not already
        # have one.
        if not hasattr(self, "_grpc_channel"):
            self._grpc_channel = self.create_channel(
                self._host, credentials=self._credentials,
            )

        # Return the channel from cache.
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsAsyncClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Sanity check: Only create a new client if we do not already have one.
        if "operations_client" not in self.__dict__:
            self.__dict__["operations_client"] = operations_v1.OperationsAsyncClient(
                self.grpc_channel
            )

        # Return the client from cache.
        return self.__dict__["operations_client"]

    @property
    def list_instances(
        self,
    ) -> Callable[
        [service.ListInstancesRequest], Awaitable[service.ListInstancesResponse]
    ]:
        r"""Return a callable for the list instances method over gRPC.

        Lists instances in a given project and location.

        Returns:
            Callable[[~.ListInstancesRequest],
                    Awaitable[~.ListInstancesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_instances" not in self._stubs:
            self._stubs["list_instances"] = self.grpc_channel.unary_unary(
                "/google.cloud.notebooks.v1beta1.NotebookService/ListInstances",
                request_serializer=service.ListInstancesRequest.serialize,
                response_deserializer=service.ListInstancesResponse.deserialize,
            )
        return self._stubs["list_instances"]

    @property
    def get_instance(
        self,
    ) -> Callable[[service.GetInstanceRequest], Awaitable[instance.Instance]]:
        r"""Return a callable for the get instance method over gRPC.

        Gets details of a single Instance.

        Returns:
            Callable[[~.GetInstanceRequest],
                    Awaitable[~.Instance]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_instance" not in self._stubs:
            self._stubs["get_instance"] = self.grpc_channel.unary_unary(
                "/google.cloud.notebooks.v1beta1.NotebookService/GetInstance",
                request_serializer=service.GetInstanceRequest.serialize,
                response_deserializer=instance.Instance.deserialize,
            )
        return self._stubs["get_instance"]

    @property
    def create_instance(
        self,
    ) -> Callable[[service.CreateInstanceRequest], Awaitable[operations.Operation]]:
        r"""Return a callable for the create instance method over gRPC.

        Creates a new Instance in a given project and
        location.

        Returns:
            Callable[[~.CreateInstanceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_instance" not in self._stubs:
            self._stubs["create_instance"] = self.grpc_channel.unary_unary(
                "/google.cloud.notebooks.v1beta1.NotebookService/CreateInstance",
                request_serializer=service.CreateInstanceRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["create_instance"]

    @property
    def register_instance(
        self,
    ) -> Callable[[service.RegisterInstanceRequest], Awaitable[operations.Operation]]:
        r"""Return a callable for the register instance method over gRPC.

        Registers an existing legacy notebook instance to the
        Notebooks API server. Legacy instances are instances
        created with the legacy Compute Engine calls. They are
        not manageable by the Notebooks API out of the box. This
        call makes these instances manageable by the Notebooks
        API.

        Returns:
            Callable[[~.RegisterInstanceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "register_instance" not in self._stubs:
            self._stubs["register_instance"] = self.grpc_channel.unary_unary(
                "/google.cloud.notebooks.v1beta1.NotebookService/RegisterInstance",
                request_serializer=service.RegisterInstanceRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["register_instance"]

    @property
    def set_instance_accelerator(
        self,
    ) -> Callable[
        [service.SetInstanceAcceleratorRequest], Awaitable[operations.Operation]
    ]:
        r"""Return a callable for the set instance accelerator method over gRPC.

        Updates the guest accelerators of a single Instance.

        Returns:
            Callable[[~.SetInstanceAcceleratorRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "set_instance_accelerator" not in self._stubs:
            self._stubs["set_instance_accelerator"] = self.grpc_channel.unary_unary(
                "/google.cloud.notebooks.v1beta1.NotebookService/SetInstanceAccelerator",
                request_serializer=service.SetInstanceAcceleratorRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["set_instance_accelerator"]

    @property
    def set_instance_machine_type(
        self,
    ) -> Callable[
        [service.SetInstanceMachineTypeRequest], Awaitable[operations.Operation]
    ]:
        r"""Return a callable for the set instance machine type method over gRPC.

        Updates the machine type of a single Instance.

        Returns:
            Callable[[~.SetInstanceMachineTypeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "set_instance_machine_type" not in self._stubs:
            self._stubs["set_instance_machine_type"] = self.grpc_channel.unary_unary(
                "/google.cloud.notebooks.v1beta1.NotebookService/SetInstanceMachineType",
                request_serializer=service.SetInstanceMachineTypeRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["set_instance_machine_type"]

    @property
    def set_instance_labels(
        self,
    ) -> Callable[[service.SetInstanceLabelsRequest], Awaitable[operations.Operation]]:
        r"""Return a callable for the set instance labels method over gRPC.

        Updates the labels of an Instance.

        Returns:
            Callable[[~.SetInstanceLabelsRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "set_instance_labels" not in self._stubs:
            self._stubs["set_instance_labels"] = self.grpc_channel.unary_unary(
                "/google.cloud.notebooks.v1beta1.NotebookService/SetInstanceLabels",
                request_serializer=service.SetInstanceLabelsRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["set_instance_labels"]

    @property
    def delete_instance(
        self,
    ) -> Callable[[service.DeleteInstanceRequest], Awaitable[operations.Operation]]:
        r"""Return a callable for the delete instance method over gRPC.

        Deletes a single Instance.

        Returns:
            Callable[[~.DeleteInstanceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_instance" not in self._stubs:
            self._stubs["delete_instance"] = self.grpc_channel.unary_unary(
                "/google.cloud.notebooks.v1beta1.NotebookService/DeleteInstance",
                request_serializer=service.DeleteInstanceRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["delete_instance"]

    @property
    def start_instance(
        self,
    ) -> Callable[[service.StartInstanceRequest], Awaitable[operations.Operation]]:
        r"""Return a callable for the start instance method over gRPC.

        Starts a notebook instance.

        Returns:
            Callable[[~.StartInstanceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "start_instance" not in self._stubs:
            self._stubs["start_instance"] = self.grpc_channel.unary_unary(
                "/google.cloud.notebooks.v1beta1.NotebookService/StartInstance",
                request_serializer=service.StartInstanceRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["start_instance"]

    @property
    def stop_instance(
        self,
    ) -> Callable[[service.StopInstanceRequest], Awaitable[operations.Operation]]:
        r"""Return a callable for the stop instance method over gRPC.

        Stops a notebook instance.

        Returns:
            Callable[[~.StopInstanceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "stop_instance" not in self._stubs:
            self._stubs["stop_instance"] = self.grpc_channel.unary_unary(
                "/google.cloud.notebooks.v1beta1.NotebookService/StopInstance",
                request_serializer=service.StopInstanceRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["stop_instance"]

    @property
    def reset_instance(
        self,
    ) -> Callable[[service.ResetInstanceRequest], Awaitable[operations.Operation]]:
        r"""Return a callable for the reset instance method over gRPC.

        Resets a notebook instance.

        Returns:
            Callable[[~.ResetInstanceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "reset_instance" not in self._stubs:
            self._stubs["reset_instance"] = self.grpc_channel.unary_unary(
                "/google.cloud.notebooks.v1beta1.NotebookService/ResetInstance",
                request_serializer=service.ResetInstanceRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["reset_instance"]

    @property
    def report_instance_info(
        self,
    ) -> Callable[[service.ReportInstanceInfoRequest], Awaitable[operations.Operation]]:
        r"""Return a callable for the report instance info method over gRPC.

        Allows notebook instances to
        report their latest instance information to the
        Notebooks API server. The server will merge the reported
        information to the instance metadata store. Do not use
        this method directly.

        Returns:
            Callable[[~.ReportInstanceInfoRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "report_instance_info" not in self._stubs:
            self._stubs["report_instance_info"] = self.grpc_channel.unary_unary(
                "/google.cloud.notebooks.v1beta1.NotebookService/ReportInstanceInfo",
                request_serializer=service.ReportInstanceInfoRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["report_instance_info"]

    @property
    def is_instance_upgradeable(
        self,
    ) -> Callable[
        [service.IsInstanceUpgradeableRequest],
        Awaitable[service.IsInstanceUpgradeableResponse],
    ]:
        r"""Return a callable for the is instance upgradeable method over gRPC.

        Check if a notebook instance is upgradable.

        Returns:
            Callable[[~.IsInstanceUpgradeableRequest],
                    Awaitable[~.IsInstanceUpgradeableResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "is_instance_upgradeable" not in self._stubs:
            self._stubs["is_instance_upgradeable"] = self.grpc_channel.unary_unary(
                "/google.cloud.notebooks.v1beta1.NotebookService/IsInstanceUpgradeable",
                request_serializer=service.IsInstanceUpgradeableRequest.serialize,
                response_deserializer=service.IsInstanceUpgradeableResponse.deserialize,
            )
        return self._stubs["is_instance_upgradeable"]

    @property
    def upgrade_instance(
        self,
    ) -> Callable[[service.UpgradeInstanceRequest], Awaitable[operations.Operation]]:
        r"""Return a callable for the upgrade instance method over gRPC.

        Upgrades a notebook instance to the latest version.

        Returns:
            Callable[[~.UpgradeInstanceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "upgrade_instance" not in self._stubs:
            self._stubs["upgrade_instance"] = self.grpc_channel.unary_unary(
                "/google.cloud.notebooks.v1beta1.NotebookService/UpgradeInstance",
                request_serializer=service.UpgradeInstanceRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["upgrade_instance"]

    @property
    def upgrade_instance_internal(
        self,
    ) -> Callable[
        [service.UpgradeInstanceInternalRequest], Awaitable[operations.Operation]
    ]:
        r"""Return a callable for the upgrade instance internal method over gRPC.

        Allows notebook instances to
        call this endpoint to upgrade themselves. Do not use
        this method directly.

        Returns:
            Callable[[~.UpgradeInstanceInternalRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "upgrade_instance_internal" not in self._stubs:
            self._stubs["upgrade_instance_internal"] = self.grpc_channel.unary_unary(
                "/google.cloud.notebooks.v1beta1.NotebookService/UpgradeInstanceInternal",
                request_serializer=service.UpgradeInstanceInternalRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["upgrade_instance_internal"]

    @property
    def list_environments(
        self,
    ) -> Callable[
        [service.ListEnvironmentsRequest], Awaitable[service.ListEnvironmentsResponse]
    ]:
        r"""Return a callable for the list environments method over gRPC.

        Lists environments in a project.

        Returns:
            Callable[[~.ListEnvironmentsRequest],
                    Awaitable[~.ListEnvironmentsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_environments" not in self._stubs:
            self._stubs["list_environments"] = self.grpc_channel.unary_unary(
                "/google.cloud.notebooks.v1beta1.NotebookService/ListEnvironments",
                request_serializer=service.ListEnvironmentsRequest.serialize,
                response_deserializer=service.ListEnvironmentsResponse.deserialize,
            )
        return self._stubs["list_environments"]

    @property
    def get_environment(
        self,
    ) -> Callable[[service.GetEnvironmentRequest], Awaitable[environment.Environment]]:
        r"""Return a callable for the get environment method over gRPC.

        Gets details of a single Environment.

        Returns:
            Callable[[~.GetEnvironmentRequest],
                    Awaitable[~.Environment]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_environment" not in self._stubs:
            self._stubs["get_environment"] = self.grpc_channel.unary_unary(
                "/google.cloud.notebooks.v1beta1.NotebookService/GetEnvironment",
                request_serializer=service.GetEnvironmentRequest.serialize,
                response_deserializer=environment.Environment.deserialize,
            )
        return self._stubs["get_environment"]

    @property
    def create_environment(
        self,
    ) -> Callable[[service.CreateEnvironmentRequest], Awaitable[operations.Operation]]:
        r"""Return a callable for the create environment method over gRPC.

        Creates a new Environment.

        Returns:
            Callable[[~.CreateEnvironmentRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_environment" not in self._stubs:
            self._stubs["create_environment"] = self.grpc_channel.unary_unary(
                "/google.cloud.notebooks.v1beta1.NotebookService/CreateEnvironment",
                request_serializer=service.CreateEnvironmentRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["create_environment"]

    @property
    def delete_environment(
        self,
    ) -> Callable[[service.DeleteEnvironmentRequest], Awaitable[operations.Operation]]:
        r"""Return a callable for the delete environment method over gRPC.

        Deletes a single Environment.

        Returns:
            Callable[[~.DeleteEnvironmentRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_environment" not in self._stubs:
            self._stubs["delete_environment"] = self.grpc_channel.unary_unary(
                "/google.cloud.notebooks.v1beta1.NotebookService/DeleteEnvironment",
                request_serializer=service.DeleteEnvironmentRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs["delete_environment"]


__all__ = ("NotebookServiceGrpcAsyncIOTransport",)
