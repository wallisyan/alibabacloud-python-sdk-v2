# Copyright 2019 Alibaba Cloud Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from alibabacloud.exceptions import ClientException
from alibabacloud.resources.base import ServiceResource
from alibabacloud.resources.collection import _create_resource_collection, \
    _create_special_resource_collection
from alibabacloud.utils.utils import _new_get_key_in_response, _transfer_params


class _RDSResource(ServiceResource):

    def __init__(self, _client=None):
        ServiceResource.__init__(self, 'rds', _client=_client)
        self.backups = _create_resource_collection(
            _RDSBackupResource, _client, _client.describe_backups,
            'Items.Backup', 'BackupId',
        )
        self.db_instances = _create_resource_collection(
            _RDSDBInstanceResource, _client, _client.describe_db_instances,
            'Items.DBInstance', 'DBInstanceId',
        )
        self.migrate_tasks = _create_resource_collection(
            _RDSMigrateTaskResource, _client, _client.describe_migrate_tasks,
            'Items.MigrateTask', 'MigrateTaskId',
        )
        self.regions = _create_special_resource_collection(
            _RDSRegionResource, _client, _client.describe_regions,
            'Regions.RDSRegion', 'RegionId',
        )
        self.slow_logs = _create_resource_collection(
            _RDSSlowLogResource, _client, _client.describe_slow_logs,
            'Items.SQLSlowLog', 'SlowLogId',
        )
        self.tasks = _create_resource_collection(
            _RDSTaskResource, _client, _client.describe_tasks,
            'Items.TaskProgressInfo', 'TaskId',
        )

    def create_db_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_db_instance(**_params)
        db_instance_id = _new_get_key_in_response(response, 'DBInstanceId')
        return _RDSDBInstanceResource(db_instance_id, _client=self._client)

    def create_db_instance_replica(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_db_instance_replica(**_params)
        workflow_id = _new_get_key_in_response(response, 'WorkflowId')
        return _RDSDBInstanceReplicaResource(workflow_id, _client=self._client)

    def create_migrate_task(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_migrate_task(**_params)
        migrate_task_id = _new_get_key_in_response(response, 'MigrateTaskId')
        return _RDSMigrateTaskResource(migrate_task_id, _client=self._client)

    def create_migrate_task_for_sql_server(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_migrate_task_for_sql_server(**_params)
        migrate_iask_id = _new_get_key_in_response(response, 'MigrateIaskId')
        return _RDSMigrateTaskForSQLServerResource(migrate_iask_id, _client=self._client)

    def create_read_only_db_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_read_only_db_instance(**_params)
        order_id = _new_get_key_in_response(response, 'OrderId')
        return _RDSReadOnlyDBInstanceResource(order_id, _client=self._client)

    def create_temp_db_instance(self, **params):
        _params = _transfer_params(params)
        response = self._client.create_temp_db_instance(**_params)
        temp_db_instance_id = _new_get_key_in_response(response, 'TempDBInstanceId')
        return _RDSTempDBInstanceResource(temp_db_instance_id, _client=self._client)


class _RDSBackupResource(ServiceResource):

    def __init__(self, backup_id, _client=None):
        ServiceResource.__init__(self, "rds.backup", _client=_client)
        self.backup_id = backup_id

        self.backup_db_names = None
        self.backup_download_url = None
        self.backup_end_time = None
        self.backup_extraction_status = None
        self.backup_intranet_download_url = None
        self.backup_location = None
        self.backup_method = None
        self.backup_mode = None
        self.backup_scale = None
        self.backup_size = None
        self.backup_start_time = None
        self.backup_status = None
        self.backup_type = None
        self.db_instance_id = None
        self.host_instance_id = None
        self.meta_status = None
        self.slave_status = None
        self.store_status = None
        self.total_backup_size = None

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_backup(backup_id=self.backup_id, **_params)

    def refresh(self):
        result = self._client.describe_backups(backup_id=self.backup_id)
        items = _new_get_key_in_response(result, 'Items.Backup')
        if not items:
            raise ClientException(msg=
                                  "Failed to find backup data from DescribeBackups response. "
                                  "BackupId = {0}".format(self.backup_id))
        self._assign_attributes(items[0])


class _RDSCrossBackupResource(ServiceResource):

    def __init__(self, cross_backup_id, _client=None):
        ServiceResource.__init__(self, "rds.cross_backup", _client=_client)
        self.cross_backup_id = cross_backup_id

    def describe_available_recovery_time(self, **params):
        _params = _transfer_params(params)
        self._client.describe_available_recovery_time(cross_backup_id=self.cross_backup_id,
                                                      **_params)


class _RDSDBInstanceResource(ServiceResource):

    def __init__(self, db_instance_id, _client=None):
        ServiceResource.__init__(self, "rds.db_instance", _client=_client)
        self.db_instance_id = db_instance_id

        self.auto_upgrade_minor_version = None
        self.category = None
        self.connection_mode = None
        self.create_time = None
        self.db_instance_class = None
        self.db_instance_description = None
        self.db_instance_net_type = None
        self.db_instance_status = None
        self.db_instance_storage_type = None
        self.db_instance_type = None
        self.destroy_time = None
        self.engine = None
        self.engine_version = None
        self.expire_time = None
        self.guard_db_instance_id = None
        self.ins_id = None
        self.instance_network_type = None
        self.lock_mode = None
        self.lock_reason = None
        self.master_instance_id = None
        self.mutri_orsignle = None
        self.pay_type = None
        self.read_only_db_instance_ids = None
        self.region_id = None
        self.replicate_id = None
        self.resource_group_id = None
        self.temp_db_instance_id = None
        self.vswitch_id = None
        self.vpc_cloud_instance_id = None
        self.vpc_id = None
        self.zone_id = None

    def add_tags_to_resource(self, **params):
        _params = _transfer_params(params)
        self._client.add_tags_to_resource(db_instance_id=self.db_instance_id, **_params)

    def allocate_instance_private_connection(self, **params):
        _params = _transfer_params(params)
        self._client.allocate_instance_private_connection(db_instance_id=self.db_instance_id,
                                                          **_params)

    def allocate_instance_public_connection(self, **params):
        _params = _transfer_params(params)
        self._client.allocate_instance_public_connection(db_instance_id=self.db_instance_id,
                                                         **_params)

    def allocate_instance_vpc_network_type(self, **params):
        _params = _transfer_params(params)
        self._client.allocate_instance_vpc_network_type(db_instance_id=self.db_instance_id,
                                                        **_params)

    def allocate_read_write_splitting_connection(self, **params):
        _params = _transfer_params(params)
        self._client.allocate_read_write_splitting_connection(db_instance_id=self.db_instance_id,
                                                              **_params)

    def calculate_db_instance_weight(self, **params):
        _params = _transfer_params(params)
        self._client.calculate_db_instance_weight(db_instance_id=self.db_instance_id, **_params)

    def check_account_name_available(self, **params):
        _params = _transfer_params(params)
        self._client.check_account_name_available(db_instance_id=self.db_instance_id, **_params)

    def check_instance_exist(self, **params):
        _params = _transfer_params(params)
        self._client.check_instance_exist(db_instance_id=self.db_instance_id, **_params)

    def check_recovery_conditions(self, **params):
        _params = _transfer_params(params)
        self._client.check_recovery_conditions(db_instance_id=self.db_instance_id, **_params)

    def copy_database_between_instances(self, **params):
        _params = _transfer_params(params)
        self._client.copy_database_between_instances(db_instance_id=self.db_instance_id, **_params)

    def create_account(self, **params):
        _params = _transfer_params(params)
        self._client.create_account(db_instance_id=self.db_instance_id, **_params)

    def create_database(self, **params):
        _params = _transfer_params(params)
        self._client.create_database(db_instance_id=self.db_instance_id, **_params)

    def create_diagnostic_report(self, **params):
        _params = _transfer_params(params)
        self._client.create_diagnostic_report(db_instance_id=self.db_instance_id, **_params)

    def delete(self, **params):
        _params = _transfer_params(params)
        self._client.delete_db_instance(db_instance_id=self.db_instance_id, **_params)

    def delete_account(self, **params):
        _params = _transfer_params(params)
        self._client.delete_account(db_instance_id=self.db_instance_id, **_params)

    def delete_database(self, **params):
        _params = _transfer_params(params)
        self._client.delete_database(db_instance_id=self.db_instance_id, **_params)

    def describe_backup_database(self, **params):
        _params = _transfer_params(params)
        self._client.describe_backup_database(db_instance_id=self.db_instance_id, **_params)

    def describe_backup_policy(self, **params):
        _params = _transfer_params(params)
        self._client.describe_backup_policy(db_instance_id=self.db_instance_id, **_params)

    def describe_cloud_db_expert_service(self, **params):
        _params = _transfer_params(params)
        self._client.describe_cloud_db_expert_service(db_instance_id=self.db_instance_id, **_params)

    def describe_db_instance_ip_hostname(self, **params):
        _params = _transfer_params(params)
        self._client.describe_db_instance_ip_hostname(db_instance_id=self.db_instance_id, **_params)

    def describe_db_instance_monitor(self, **params):
        _params = _transfer_params(params)
        self._client.describe_db_instance_monitor(db_instance_id=self.db_instance_id, **_params)

    def describe_db_instance_proxy_configuration(self, **params):
        _params = _transfer_params(params)
        self._client.describe_db_instance_proxy_configuration(db_instance_id=self.db_instance_id,
                                                              **_params)

    def describe_db_instance_ssl(self, **params):
        _params = _transfer_params(params)
        self._client.describe_db_instance_ssl(db_instance_id=self.db_instance_id, **_params)

    def describe_instance_cross_backup_policy(self, **params):
        _params = _transfer_params(params)
        self._client.describe_instance_cross_backup_policy(db_instance_id=self.db_instance_id,
                                                           **_params)

    def describe_proxy_function_support(self, **params):
        _params = _transfer_params(params)
        self._client.describe_proxy_function_support(db_instance_id=self.db_instance_id, **_params)

    def describe_resource_usage(self, **params):
        _params = _transfer_params(params)
        self._client.describe_resource_usage(db_instance_id=self.db_instance_id, **_params)

    def grant_account_privilege(self, **params):
        _params = _transfer_params(params)
        self._client.grant_account_privilege(db_instance_id=self.db_instance_id, **_params)

    def grant_operator_permission(self, **params):
        _params = _transfer_params(params)
        self._client.grant_operator_permission(db_instance_id=self.db_instance_id, **_params)

    def import_data_for_sql_server(self, **params):
        _params = _transfer_params(params)
        self._client.import_data_for_sql_server(db_instance_id=self.db_instance_id, **_params)

    def import_database_between_instances(self, **params):
        _params = _transfer_params(params)
        self._client.import_database_between_instances(db_instance_id=self.db_instance_id,
                                                       **_params)

    def migrate_security_ip_mode(self, **params):
        _params = _transfer_params(params)
        self._client.migrate_security_ip_mode(db_instance_id=self.db_instance_id, **_params)

    def migrate_to_other_region(self, **params):
        _params = _transfer_params(params)
        self._client.migrate_to_other_region(db_instance_id=self.db_instance_id, **_params)

    def modify_account_description(self, **params):
        _params = _transfer_params(params)
        self._client.modify_account_description(db_instance_id=self.db_instance_id, **_params)

    def modify_auto_upgrade_minor_version(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_auto_upgrade_minor_version(
            db_instance_id=self.db_instance_id, **_params)

    def modify_backup_policy(self, **params):
        _params = _transfer_params(params)
        self._client.modify_backup_policy(db_instance_id=self.db_instance_id, **_params)

    def modify_collation_time_zone(self, **params):
        _params = _transfer_params(params)
        self._client.modify_collation_time_zone(db_instance_id=self.db_instance_id, **_params)

    def modify_connection_mode(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_connection_mode(db_instance_id=self.db_instance_id,
                                                        **_params)

    def modify_connection_string(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_connection_string(db_instance_id=self.db_instance_id,
                                                          **_params)

    def modify_db_description(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_description(db_instance_id=self.db_instance_id, **_params)

    def modify_dtc_security_ip_hosts_for_sql_server(self, **params):
        _params = _transfer_params(params)
        self._client.modify_dtc_security_ip_hosts_for_sql_server(db_instance_id=self.db_instance_id,
                                                                 **_params)

    def modify_description(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_description(db_instance_id=self.db_instance_id, **_params)

    def modify_instance_auto_renewal_attribute(self, **params):
        _params = _transfer_params(params)
        self._client.modify_instance_auto_renewal_attribute(db_instance_id=self.db_instance_id,
                                                            **_params)

    def modify_instance_cross_backup_policy(self, **params):
        _params = _transfer_params(params)
        self._client.modify_instance_cross_backup_policy(db_instance_id=self.db_instance_id,
                                                         **_params)

    def modify_maintain_time(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_maintain_time(db_instance_id=self.db_instance_id, **_params)

    def modify_monitor(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_monitor(db_instance_id=self.db_instance_id, **_params)

    def modify_my_sqldb_instance_delay(self, **params):
        _params = _transfer_params(params)
        self._client.modify_my_sqldb_instance_delay(db_instance_id=self.db_instance_id, **_params)

    def modify_network_expire_time(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_network_expire_time(db_instance_id=self.db_instance_id,
                                                            **_params)

    def modify_network_type(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_network_type(db_instance_id=self.db_instance_id, **_params)

    def modify_parameter(self, **params):
        _params = _transfer_params(params)
        self._client.modify_parameter(db_instance_id=self.db_instance_id, **_params)

    def modify_pay_type(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_pay_type(db_instance_id=self.db_instance_id, **_params)

    def modify_proxy_configuration(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_proxy_configuration(db_instance_id=self.db_instance_id,
                                                            **_params)

    def modify_read_write_splitting_connection(self, **params):
        _params = _transfer_params(params)
        self._client.modify_read_write_splitting_connection(db_instance_id=self.db_instance_id,
                                                            **_params)

    def modify_readonly_instance_delay_replication_time(self, **params):
        _params = _transfer_params(params)
        self._client.modify_readonly_instance_delay_replication_time(
            db_instance_id=self.db_instance_id, **_params)

    def modify_sql_collector_policy(self, **params):
        _params = _transfer_params(params)
        self._client.modify_sql_collector_policy(db_instance_id=self.db_instance_id, **_params)

    def modify_ssl(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_ssl(db_instance_id=self.db_instance_id, **_params)

    def modify_security_ips(self, **params):
        _params = _transfer_params(params)
        self._client.modify_security_ips(db_instance_id=self.db_instance_id, **_params)

    def modify_spec(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_spec(db_instance_id=self.db_instance_id, **_params)

    def modify_tde(self, **params):
        _params = _transfer_params(params)
        self._client.modify_db_instance_tde(db_instance_id=self.db_instance_id, **_params)

    def purge_db_instance_log(self, **params):
        _params = _transfer_params(params)
        self._client.purge_db_instance_log(db_instance_id=self.db_instance_id, **_params)

    def release_instance_public_connection(self, **params):
        _params = _transfer_params(params)
        self._client.release_instance_public_connection(db_instance_id=self.db_instance_id,
                                                        **_params)

    def release_read_write_splitting_connection(self, **params):
        _params = _transfer_params(params)
        self._client.release_read_write_splitting_connection(db_instance_id=self.db_instance_id,
                                                             **_params)

    def remove_tags_from_resource(self, **params):
        _params = _transfer_params(params)
        self._client.remove_tags_from_resource(db_instance_id=self.db_instance_id, **_params)

    def renew_instance(self, **params):
        _params = _transfer_params(params)
        self._client.renew_instance(db_instance_id=self.db_instance_id, **_params)

    def request_service_of_cloud_db_expert(self, **params):
        _params = _transfer_params(params)
        self._client.request_service_of_cloud_db_expert(db_instance_id=self.db_instance_id,
                                                        **_params)

    def reset_account(self, **params):
        _params = _transfer_params(params)
        self._client.reset_account(db_instance_id=self.db_instance_id, **_params)

    def reset_account_for_pg(self, **params):
        _params = _transfer_params(params)
        self._client.reset_account_for_pg(db_instance_id=self.db_instance_id, **_params)

    def reset_account_password(self, **params):
        _params = _transfer_params(params)
        self._client.reset_account_password(db_instance_id=self.db_instance_id, **_params)

    def restart(self, **params):
        _params = _transfer_params(params)
        self._client.restart_db_instance(db_instance_id=self.db_instance_id, **_params)

    def restore(self, **params):
        _params = _transfer_params(params)
        self._client.restore_db_instance(db_instance_id=self.db_instance_id, **_params)

    def restore_table(self, **params):
        _params = _transfer_params(params)
        self._client.restore_table(db_instance_id=self.db_instance_id, **_params)

    def revoke_account_privilege(self, **params):
        _params = _transfer_params(params)
        self._client.revoke_account_privilege(db_instance_id=self.db_instance_id, **_params)

    def revoke_operator_permission(self, **params):
        _params = _transfer_params(params)
        self._client.revoke_operator_permission(db_instance_id=self.db_instance_id, **_params)

    def switch_db_instance_ha(self, **params):
        _params = _transfer_params(params)
        self._client.switch_db_instance_ha(db_instance_id=self.db_instance_id, **_params)

    def switch_db_instance_net_type(self, **params):
        _params = _transfer_params(params)
        self._client.switch_db_instance_net_type(db_instance_id=self.db_instance_id, **_params)

    def switch_db_instance_vpc(self, **params):
        _params = _transfer_params(params)
        self._client.switch_db_instance_vpc(db_instance_id=self.db_instance_id, **_params)

    def upgrade_db_instance_engine_version(self, **params):
        _params = _transfer_params(params)
        self._client.upgrade_db_instance_engine_version(db_instance_id=self.db_instance_id,
                                                        **_params)

    def upgrade_db_instance_kernel_version(self, **params):
        _params = _transfer_params(params)
        self._client.upgrade_db_instance_kernel_version(db_instance_id=self.db_instance_id,
                                                        **_params)

    def refresh(self):
        result = self._client.describe_db_instances(db_instance_id=self.db_instance_id)
        items = _new_get_key_in_response(result, 'Items.DBInstance')
        if not items:
            raise ClientException(msg=
                                  "Failed to find db_instance data from DescribeDBInstances response. "
                                  "DBInstanceId = {0}".format(self.db_instance_id))
        self._assign_attributes(items[0])


class _RDSDBInstanceReplicaResource(ServiceResource):

    def __init__(self, workflow_id, _client=None):
        ServiceResource.__init__(self, "rds.db_instance_replica", _client=_client)
        self.workflow_id = workflow_id


class _RDSMigrateTaskResource(ServiceResource):

    def __init__(self, migrate_task_id, _client=None):
        ServiceResource.__init__(self, "rds.migrate_task", _client=_client)
        self.migrate_task_id = migrate_task_id

        self.backup_mode = None
        self.create_time = None
        self.db_name = None
        self.description = None
        self.end_time = None
        self.is_db_replaced = None
        self.status = None

    def create_online_database_task(self, **params):
        _params = _transfer_params(params)
        self._client.create_online_database_task(migrate_task_id=self.migrate_task_id, **_params)


class _RDSMigrateTaskForSQLServerResource(ServiceResource):

    def __init__(self, migrate_iask_id, _client=None):
        ServiceResource.__init__(self, "rds.migrate_task_for_sql_server", _client=_client)
        self.migrate_iask_id = migrate_iask_id


class _RDSReadOnlyDBInstanceResource(ServiceResource):

    def __init__(self, order_id, _client=None):
        ServiceResource.__init__(self, "rds.read_only_db_instance", _client=_client)
        self.order_id = order_id


class _RDSRegionResource(ServiceResource):

    def __init__(self, region_id, _client=None):
        ServiceResource.__init__(self, "rds.region", _client=_client)
        self.region_id = region_id

        self.local_name = None
        self.region_endpoint = None
        self.status = None

    def refresh(self):
        result = self._client.describe_regions(region_id=self.region_id)
        items = _new_get_key_in_response(result, 'Regions.Region')
        if not items:
            raise ClientException(msg=
                                  "Failed to find region data from DescribeRegions response. "
                                  "RegionId = {0}".format(self.region_id))
        self._assign_attributes(items[0])


class _RDSReplicaResource(ServiceResource):

    def __init__(self, replica_id, _client=None):
        ServiceResource.__init__(self, "rds.replica", _client=_client)
        self.replica_id = replica_id

    def modify_description(self, **params):
        _params = _transfer_params(params)
        self._client.modify_replica_description(replica_id=self.replica_id, **_params)


class _RDSSlowLogResource(ServiceResource):

    def __init__(self, slow_log_id, _client=None):
        ServiceResource.__init__(self, "rds.slow_log", _client=_client)
        self.slow_log_id = slow_log_id

        self.avg_execution_time = None
        self.create_time = None
        self.db_name = None
        self.max_execution_time = None
        self.max_lock_time = None
        self.my_sql_total_execution_counts = None
        self.my_sql_total_execution_times = None
        self.parse_max_row_count = None
        self.parse_total_row_counts = None
        self.report_time = None
        self.return_max_row_count = None
        self.return_total_row_counts = None
        self.sqlhash = None
        self.sql_id_str = None
        self.sql_server_total_execution_counts = None
        self.sql_server_total_execution_times = None
        self.sql_text = None
        self.total_lock_times = None
        self.total_logical_read_counts = None
        self.total_physical_read_counts = None


class _RDSTaskResource(ServiceResource):

    def __init__(self, task_id, _client=None):
        ServiceResource.__init__(self, "rds.task", _client=_client)
        self.task_id = task_id

        self.creation_time = None
        self.finished_time = None
        self.support_cancel = None
        self.task_action = None
        self.task_status = None

    def refresh(self):
        result = self._client.describe_tasks(task_ids=self.task_id)
        items = _new_get_key_in_response(result, 'TaskSet.Task')
        if not items:
            raise ClientException(msg=
                                  "Failed to find task data from DescribeTasks response. "
                                  "TaskId = {0}".format(self.task_id))
        self._assign_attributes(items[0])


class _RDSTempDBInstanceResource(ServiceResource):

    def __init__(self, temp_db_instance_id, _client=None):
        ServiceResource.__init__(self, "rds.temp_db_instance", _client=_client)
        self.temp_db_instance_id = temp_db_instance_id


class _RDSZoneResource(ServiceResource):

    def __init__(self, zone_id, _client=None):
        ServiceResource.__init__(self, "rds.zone", _client=_client)
        self.zone_id = zone_id

    def check_resource(self, **params):
        _params = _transfer_params(params)
        self._client.check_resource(zone_id=self.zone_id, **_params)

    def migrate_to_other(self, **params):
        _params = _transfer_params(params)
        self._client.migrate_to_other_zone(zone_id=self.zone_id, **_params)
