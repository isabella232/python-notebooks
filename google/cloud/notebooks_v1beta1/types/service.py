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

import proto  # type: ignore


from google.cloud.notebooks_v1beta1.types import environment as gcn_environment
from google.cloud.notebooks_v1beta1.types import instance as gcn_instance
from google.protobuf import timestamp_pb2 as timestamp  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.notebooks.v1beta1',
    manifest={
        'OperationMetadata',
        'ListInstancesRequest',
        'ListInstancesResponse',
        'GetInstanceRequest',
        'CreateInstanceRequest',
        'RegisterInstanceRequest',
        'SetInstanceAcceleratorRequest',
        'SetInstanceMachineTypeRequest',
        'SetInstanceLabelsRequest',
        'DeleteInstanceRequest',
        'StartInstanceRequest',
        'StopInstanceRequest',
        'ResetInstanceRequest',
        'ReportInstanceInfoRequest',
        'IsInstanceUpgradeableRequest',
        'IsInstanceUpgradeableResponse',
        'UpgradeInstanceRequest',
        'UpgradeInstanceInternalRequest',
        'ListEnvironmentsRequest',
        'ListEnvironmentsResponse',
        'GetEnvironmentRequest',
        'CreateEnvironmentRequest',
        'DeleteEnvironmentRequest',
    },
)


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (~.timestamp.Timestamp):
            The time the operation was created.
        end_time (~.timestamp.Timestamp):
            The time the operation finished running.
        target (str):
            Server-defined resource path for the target
            of the operation.
        verb (str):
            Name of the verb executed by the operation.
        status_message (str):
            Human-readable status of the operation, if
            any.
        requested_cancellation (bool):
            Identifies whether the user has requested cancellation of
            the operation. Operations that have successfully been
            cancelled have [Operation.error][] value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            API version used to start the operation.
    """

    create_time = proto.Field(proto.MESSAGE, number=1,
        message=timestamp.Timestamp,
    )

    end_time = proto.Field(proto.MESSAGE, number=2,
        message=timestamp.Timestamp,
    )

    target = proto.Field(proto.STRING, number=3)

    verb = proto.Field(proto.STRING, number=4)

    status_message = proto.Field(proto.STRING, number=5)

    requested_cancellation = proto.Field(proto.BOOL, number=6)

    api_version = proto.Field(proto.STRING, number=7)


class ListInstancesRequest(proto.Message):
    r"""Request for listing notebook instances.

    Attributes:
        parent (str):
            Required. Format:
            ``parent=projects/{project_id}/locations/{location}``
        page_size (int):
            Maximum return size of the list call.
        page_token (str):
            A previous returned page token that can be
            used to continue listing from the last result.
    """

    parent = proto.Field(proto.STRING, number=1)

    page_size = proto.Field(proto.INT32, number=2)

    page_token = proto.Field(proto.STRING, number=3)


class ListInstancesResponse(proto.Message):
    r"""Response for listing notebook instances.

    Attributes:
        instances (Sequence[~.gcn_instance.Instance]):
            A list of returned instances.
        next_page_token (str):
            Page token that can be used to continue
            listing from the last result in the next list
            call.
        unreachable (Sequence[str]):
            Locations that could not be reached. For example,
            ['us-west1-a', 'us-central1-b']. A ListInstancesResponse
            will only contain either instances or unreachables,
    """

    @property
    def raw_page(self):
        return self

    instances = proto.RepeatedField(proto.MESSAGE, number=1,
        message=gcn_instance.Instance,
    )

    next_page_token = proto.Field(proto.STRING, number=2)

    unreachable = proto.RepeatedField(proto.STRING, number=3)


class GetInstanceRequest(proto.Message):
    r"""Request for getting a notebook instance.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
    """

    name = proto.Field(proto.STRING, number=1)


class CreateInstanceRequest(proto.Message):
    r"""Request for creating a notebook instance.

    Attributes:
        parent (str):
            Required. Format:
            ``parent=projects/{project_id}/locations/{location}``
        instance_id (str):
            Required. User-defined unique ID of this
            instance.
        instance (~.gcn_instance.Instance):
            Required. The instance to be created.
    """

    parent = proto.Field(proto.STRING, number=1)

    instance_id = proto.Field(proto.STRING, number=2)

    instance = proto.Field(proto.MESSAGE, number=3,
        message=gcn_instance.Instance,
    )


class RegisterInstanceRequest(proto.Message):
    r"""Request for registering a notebook instance.

    Attributes:
        parent (str):
            Required. Format:
            ``parent=projects/{project_id}/locations/{location}``
        instance_id (str):
            Required. User defined unique ID of this instance. The
            ``instance_id`` must be 1 to 63 characters long and contain
            only lowercase letters, numeric characters, and dashes. The
            first character must be a lowercase letter and the last
            character cannot be a dash.
    """

    parent = proto.Field(proto.STRING, number=1)

    instance_id = proto.Field(proto.STRING, number=2)


class SetInstanceAcceleratorRequest(proto.Message):
    r"""Request for setting instance accelerator.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
        type (~.gcn_instance.Instance.AcceleratorType):
            Required. Type of this accelerator.
        core_count (int):
            Required. Count of cores of this accelerator. Note that not
            all combinations of ``type`` and ``core_count`` are valid.
            Check `GPUs on Compute
            Engine </compute/docs/gpus/#gpus-list>`__ to find a valid
            combination. TPUs are not supported.
    """

    name = proto.Field(proto.STRING, number=1)

    type = proto.Field(proto.ENUM, number=2,
        enum=gcn_instance.Instance.AcceleratorType,
    )

    core_count = proto.Field(proto.INT64, number=3)


class SetInstanceMachineTypeRequest(proto.Message):
    r"""Request for setting instance machine type.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
        machine_type (str):
            Required. The `Compute Engine machine
            type </compute/docs/machine-types>`__.
    """

    name = proto.Field(proto.STRING, number=1)

    machine_type = proto.Field(proto.STRING, number=2)


class SetInstanceLabelsRequest(proto.Message):
    r"""Request for setting instance labels.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
        labels (Sequence[~.service.SetInstanceLabelsRequest.LabelsEntry]):
            Labels to apply to this instance.
            These can be later modified by the setLabels
            method
    """

    name = proto.Field(proto.STRING, number=1)

    labels = proto.MapField(proto.STRING, proto.STRING, number=2)


class DeleteInstanceRequest(proto.Message):
    r"""Request for deleting a notebook instance.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
    """

    name = proto.Field(proto.STRING, number=1)


class StartInstanceRequest(proto.Message):
    r"""Request for starting a notebook instance

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
    """

    name = proto.Field(proto.STRING, number=1)


class StopInstanceRequest(proto.Message):
    r"""Request for stopping a notebook instance

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
    """

    name = proto.Field(proto.STRING, number=1)


class ResetInstanceRequest(proto.Message):
    r"""Request for reseting a notebook instance

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
    """

    name = proto.Field(proto.STRING, number=1)


class ReportInstanceInfoRequest(proto.Message):
    r"""Request for notebook instances to report information to
    Notebooks API.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
        vm_id (str):
            Required. The VM hardware token for
            authenticating the VM.
            https://cloud.google.com/compute/docs/instances/verifying-
            instance-identity
        metadata (Sequence[~.service.ReportInstanceInfoRequest.MetadataEntry]):
            The metadata reported to Notebooks API. This
            will be merged to the instance metadata store
    """

    name = proto.Field(proto.STRING, number=1)

    vm_id = proto.Field(proto.STRING, number=2)

    metadata = proto.MapField(proto.STRING, proto.STRING, number=3)


class IsInstanceUpgradeableRequest(proto.Message):
    r"""Request for checking if a notebook instance is upgradeable.

    Attributes:
        notebook_instance (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
    """

    notebook_instance = proto.Field(proto.STRING, number=1)


class IsInstanceUpgradeableResponse(proto.Message):
    r"""Response for checking if a notebook instance is upgradeable.

    Attributes:
        upgradeable (bool):
            If an instance is upgradeable.
        upgrade_version (str):
            The version this instance will be upgraded to
            if calling the upgrade endpoint. This field will
            only be populated if field upgradeable is true.
    """

    upgradeable = proto.Field(proto.BOOL, number=1)

    upgrade_version = proto.Field(proto.STRING, number=2)


class UpgradeInstanceRequest(proto.Message):
    r"""Request for upgrading a notebook instance

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
    """

    name = proto.Field(proto.STRING, number=1)


class UpgradeInstanceInternalRequest(proto.Message):
    r"""Request for upgrading a notebook instance from within the VM

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``
        vm_id (str):
            Required. The VM hardware token for
            authenticating the VM.
            https://cloud.google.com/compute/docs/instances/verifying-
            instance-identity
    """

    name = proto.Field(proto.STRING, number=1)

    vm_id = proto.Field(proto.STRING, number=2)


class ListEnvironmentsRequest(proto.Message):
    r"""Request for listing environments.

    Attributes:
        parent (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}``
        page_size (int):
            Maximum return size of the list call.
        page_token (str):
            A previous returned page token that can be
            used to continue listing from the last result.
    """

    parent = proto.Field(proto.STRING, number=1)

    page_size = proto.Field(proto.INT32, number=2)

    page_token = proto.Field(proto.STRING, number=3)


class ListEnvironmentsResponse(proto.Message):
    r"""Response for listing environments.

    Attributes:
        environments (Sequence[~.gcn_environment.Environment]):
            A list of returned environments.
        next_page_token (str):
            A page token that can be used to continue
            listing from the last result in the next list
            call.
        unreachable (Sequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    environments = proto.RepeatedField(proto.MESSAGE, number=1,
        message=gcn_environment.Environment,
    )

    next_page_token = proto.Field(proto.STRING, number=2)

    unreachable = proto.RepeatedField(proto.STRING, number=3)


class GetEnvironmentRequest(proto.Message):
    r"""Request for getting a notebook environment.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/environments/{environment_id}``
    """

    name = proto.Field(proto.STRING, number=1)


class CreateEnvironmentRequest(proto.Message):
    r"""Request for creating a notebook environment.

    Attributes:
        parent (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}``
        environment_id (str):
            Required. User-defined unique ID of this environment. The
            ``environment_id`` must be 1 to 63 characters long and
            contain only lowercase letters, numeric characters, and
            dashes. The first character must be a lowercase letter and
            the last character cannot be a dash.
        environment (~.gcn_environment.Environment):
            Required. The environment to be created.
    """

    parent = proto.Field(proto.STRING, number=1)

    environment_id = proto.Field(proto.STRING, number=2)

    environment = proto.Field(proto.MESSAGE, number=3,
        message=gcn_environment.Environment,
    )


class DeleteEnvironmentRequest(proto.Message):
    r"""Request for deleting a notebook environment.

    Attributes:
        name (str):
            Required. Format:
            ``projects/{project_id}/locations/{location}/environments/{environment_id}``
    """

    name = proto.Field(proto.STRING, number=1)


__all__ = tuple(sorted(__protobuf__.manifest))
