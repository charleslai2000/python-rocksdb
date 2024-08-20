from typing import Any, Dict, Iterator, List, Optional, Tuple, Union

from .interfaces import AssociativeMergeOperator as IAssociativeMergeOperator
from .interfaces import Comparator as IComparator
from .interfaces import FilterPolicy as IFilterPolicy
from .interfaces import MergeOperator as IMergeOperator
from .interfaces import SliceTransform as ISliceTransform

class PyComparator:
    def get_ob(self) -> object: ...

class PyGenericComparator(PyComparator):
    ob: object
    def __init__(self, ob: IComparator) -> None: ...
    def __dealloc__(self) -> None: ...
    def get_ob(self) -> object: ...

class PyBytewiseComparator(PyComparator):
    def __init__(self) -> None: ...
    def name(self) -> bytes: ...
    def compare(self, a: bytes, b: bytes) -> int: ...
    def get_ob(self) -> "PyBytewiseComparator": ...

class PyMergeOperator:
    ob: object

    def __init__(self, ob: IMergeOperator | IAssociativeMergeOperator) -> None: ...
    def get_ob(self) -> IMergeOperator | IAssociativeMergeOperator: ...

class PyTableFactory: ...

class BlockBasedTableFactory(PyTableFactory):
    py_filter_policy: Optional[PyFilterPolicy]

    def __init__(
        self,
        index_type: str = "binary_search",
        checksum: str = "crc32",
        block_cache: Optional[PyCache] = None,
        filter_policy: Optional[PyFilterPolicy] = None,
        no_block_cache: bool = False,
        block_size: Optional[int] = None,
        block_size_deviation: Optional[int] = None,
        block_restart_interval: Optional[int] = None,
        whole_key_filtering: Optional[bool] = None,
        cache_index_and_filter_blocks: Optional[bool] = None,
        format_version: Optional[int] = None,
    ) -> None: ...

class PlainTableFactory(PyTableFactory):
    def __init__(
        self,
        user_key_len: int = 0,
        bloom_bits_per_key: int = 10,
        hash_table_ratio: float = 0.75,
        index_sparseness: int = 10,
        huge_page_tlb_size: int = 0,
        encoding_type: str = "plain",
        full_scan_mode: bool = False,
    ) -> None: ...

class PyMemtableFactory: ...

class SkipListMemtableFactory(PyMemtableFactory):
    def __init__(self) -> None: ...

class VectorMemtableFactory(PyMemtableFactory):
    def __init__(self, count: int = 0) -> None: ...

class HashSkipListMemtableFactory(PyMemtableFactory):
    def __init__(
        self, bucket_count: int = 1000000, skiplist_height: int = 4, skiplist_branching_factor: int = 4
    ) -> None: ...

class HashLinkListMemtableFactory(PyMemtableFactory):
    def __init__(self, bucket_count: int = 50000) -> None: ...

class CompressionType:
    no_compression: str = "no_compression"
    snappy_compression: str = "snappy_compression"
    zlib_compression: str = "zlib_compression"
    bzip2_compression: str = "bzip2_compression"
    lz4_compression: str = "lz4_compression"
    lz4hc_compression: str = "lz4hc_compression"
    xpress_compression: str = "xpress_compression"
    zstd_compression: str = "zstd_compression"
    zstdnotfinal_compression: str = "zstdnotfinal_compression"
    disable_compression: str = "disable_compression"

class CompactionPri:
    by_compensated_size: str = "by_compensated_size"
    oldest_largest_seq_first: str = "oldest_largest_seq_first"
    oldest_smallest_seq_first: str = "oldest_smallest_seq_first"
    min_overlapping_ratio: str = "min_overlapping_ratio"

class PySliceTransform:
    ob: object

    def __init__(self, ob: ISliceTransform) -> None: ...
    def get_ob(self) -> ISliceTransform: ...

class PyCache: ...

class PyLRUCache(PyCache):
    def __init__(self, capacity: int, shard_bits: Optional[int] = None) -> None: ...

LRUCache = PyLRUCache

class PyFilterPolicy:
    def get_ob(self) -> object: ...

class PyGenericFilterPolicy(PyFilterPolicy):
    ob: object

    def __init__(self, ob: IFilterPolicy) -> None: ...
    def get_ob(self) -> IFilterPolicy: ...

class ColumnFamilyOptions:
    py_comparator: PyComparator
    py_merge_operator: Optional[PyMergeOperator]
    py_prefix_extractor: Optional[PySliceTransform]
    py_table_factory: Optional[PyTableFactory]
    py_memtable_factory: Optional[PyMemtableFactory]
    in_use: bool

    write_buffer_size: int
    max_write_buffer_number: int
    min_write_buffer_number_to_merge: int
    compression_opts: dict[Any, Any]
    bottommost_compression_opts: dict[Any, Any]
    compaction_pri: CompactionPri
    compression: CompressionType
    max_compaction_bytes: int
    num_levels: int
    level0_file_num_compaction_trigger: int
    level0_slowdown_writes_trigger: int
    level0_stop_writes_trigger: int
    target_file_size_base: int
    target_file_size_multiplier: int
    max_bytes_for_level_base: int
    max_bytes_for_level_multiplier: int
    max_bytes_for_level_multiplier_additional: list[Any]
    arena_block_size: int
    disable_auto_compactions: bool
    compaction_style: str
    compaction_options_universal: dict[Any, Any]
    max_sequential_skip_in_iterations: int
    inplace_update_support: bool
    inplace_update_num_locks: int
    comparator: PyComparator
    merge_operator: Optional[PyMergeOperator]
    prefix_extractor: Optional[PySliceTransform]
    optimize_filters_for_hits: bool
    paranoid_file_checks: bool

class Options(ColumnFamilyOptions):
    py_row_cache: Optional[PyCache]

    create_if_missing: bool
    create_missing_column_families: bool
    error_if_exists: bool
    paranoid_checks: bool
    max_open_files: int
    max_file_opening_threads: int
    max_total_wal_size: int
    use_fsync: bool
    db_log_dir: str
    wal_dir: str
    delete_obsolete_files_period_micros: int
    max_background_jobs: int
    max_background_compactions: int
    max_subcompactions: int
    max_background_flushes: int
    max_log_file_size: int
    log_file_time_to_roll: int
    keep_log_file_num: int
    recycle_log_file_num: int
    max_manifest_file_size: int
    table_cache_numshardbits: int
    wal_ttl_seconds: int
    wal_size_limit_mb: int
    manifest_preallocation_size: int
    allow_mmap_reads: bool
    allow_mmap_writes: bool
    use_direct_reads: bool
    use_direct_io_for_flush_and_compaction: bool
    allow_fallocate: bool
    is_fd_close_on_exec: bool
    stats_dump_period_sec: int
    stats_persist_period_sec: int
    persist_stats_to_disk: bool
    stats_history_buffer_size: int
    advise_random_on_open: bool
    db_write_buffer_size: int
    compaction_readahead_size: int
    random_access_max_buffer_size: int
    writable_file_max_buffer_size: int
    use_adaptive_mutex: bool
    bytes_per_sync: int
    wal_bytes_per_sync: int
    strict_bytes_per_sync: bool
    enable_thread_tracking: bool
    delayed_write_rate: int
    enable_pipelined_write: bool
    unordered_write: bool
    allow_concurrent_memtable_write: bool
    enable_write_thread_adaptive_yield: bool
    max_write_batch_group_size_bytes: int
    write_thread_max_yield_usec: int
    write_thread_slow_yield_usec: int
    skip_stats_update_on_db_open: bool
    skip_checking_sst_file_sizes_on_db_open: bool
    allow_2pc: bool
    row_cache: Optional[PyCache]
    fail_if_options_file_error: bool
    dump_malloc_stats: bool
    avoid_flush_during_recovery: bool
    avoid_flush_during_shutdown: bool
    allow_ingest_behind: bool
    two_write_queues: bool
    manual_wal_flush: bool
    atomic_flush: bool
    avoid_unnecessary_blocking_io: bool
    write_dbid_to_manifest: bool
    log_readahead_size: int
    best_efforts_recovery: bool

    def IncreaseParallelism(self, total_threads: int = 16) -> None: ...

class TransactionDBOptions:
    in_use: bool

    max_num_locks: int
    max_num_deadlocks: int
    num_stripes: int
    transaction_lock_timeout: int
    default_lock_timeout: int
    write_policy: str
    rollback_merge_operands: bool
    skip_concurrency_control: bool
    default_write_batch_flush_threshold: int

    def __init__(self, **kwargs: Any) -> None: ...

class ColumnFamilyHandle:
    """This represents a ColumnFamilyHandle"""

    name: bytes
    id: int

    @property
    def is_valid(self) -> bool: ...
    def __repr__(self) -> str: ...
    def get_handle(self) -> Optional[Any]: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class WriteBatch:
    def put(self, key: Union[bytes, Tuple["ColumnFamilyHandle", bytes]], value: bytes) -> None: ...
    def merge(self, key: Union[bytes, Tuple["ColumnFamilyHandle", bytes]], value: bytes) -> None: ...
    def delete(self, key: Union[bytes, Tuple["ColumnFamilyHandle", bytes]]) -> None: ...
    def clear(self) -> None: ...
    def data(self) -> bytes: ...
    def count(self) -> int: ...
    def __iter__(self) -> Iterator["WriteBatchIterator"]: ...

class WriteBatchIterator:
    def __iter__(self) -> Iterator["WriteBatchIterator"]: ...
    def __next__(
        self,
    ) -> Union[
        Tuple[str, Tuple[int, bytes], bytes], Tuple[str, bytes, bytes]  # With column family  # Without column family
    ]: ...

class Snapshot:
    db: DB

    def __init__(self, db: DB) -> None: ...
    def __dealloc__(self) -> None: ...

class DB:
    opts: Options
    def __init__(
        self,
        db_name: str,
        opts: Options,
        column_families: Optional[Dict[bytes, ColumnFamilyOptions]] = None,
        read_only: bool = False,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def close(self, safe: bool = True) -> None: ...
    @property
    def column_families(self) -> List[ColumnFamilyHandle]: ...
    def get_column_family(self, name: bytes) -> Optional[ColumnFamilyHandle]: ...
    def put(
        self,
        key: Union[bytes, Tuple[ColumnFamilyHandle, bytes]],
        value: bytes,
        sync: bool = False,
        disable_wal: bool = False,
        ignore_missing_column_families: bool = False,
        no_slowdown: bool = False,
        low_pri: bool = False,
    ) -> None: ...
    def delete(
        self,
        key: Union[bytes, Tuple[ColumnFamilyHandle, bytes]],
        sync: bool = False,
        disable_wal: bool = False,
        ignore_missing_column_families: bool = False,
        no_slowdown: bool = False,
        low_pri: bool = False,
    ) -> None: ...
    def merge(
        self,
        key: Union[bytes, Tuple[ColumnFamilyHandle, bytes]],
        value: bytes,
        sync: bool = False,
        disable_wal: bool = False,
        ignore_missing_column_families: bool = False,
        no_slowdown: bool = False,
        low_pri: bool = False,
    ) -> None: ...
    def write(
        self,
        batch: WriteBatch,
        sync: bool = False,
        disable_wal: bool = False,
        ignore_missing_column_families: bool = False,
        no_slowdown: bool = False,
        low_pri: bool = False,
    ) -> None: ...
    def get(
        self, key: Union[bytes, Tuple[ColumnFamilyHandle, bytes]], *args: Any, **kwargs: Any
    ) -> Optional[bytes]: ...
    def multi_get(
        self,
        keys: List[Union[bytes, Tuple[ColumnFamilyHandle, bytes]]],
        *args: Any,
        as_dict: bool = True,
        **kwargs: Any,
    ) -> Union[Dict[bytes, Optional[bytes]], List[Optional[bytes]]]: ...
    def key_may_exist(
        self, key: Union[bytes, Tuple[ColumnFamilyHandle, bytes]], fetch: bool = False, *args: Any, **kwargs: Any
    ) -> Tuple[bool, Optional[bytes]]: ...
    def iterkeys(self, column_family: Optional[ColumnFamilyHandle] = None, *args: Any, **kwargs: Any) -> Any: ...
    def itervalues(self, column_family: Optional[ColumnFamilyHandle] = None, *args: Any, **kwargs: Any) -> Any: ...
    def iteritems(self, column_family: Optional[ColumnFamilyHandle] = None, *args: Any, **kwargs: Any) -> Any: ...
    def iterskeys(self, column_families: List[ColumnFamilyHandle], *args: Any, **kwargs: Any) -> List[Any]: ...
    def itersvalues(self, column_families: List[ColumnFamilyHandle], *args: Any, **kwargs: Any) -> List[Any]: ...
    def itersitems(self, column_families: List[ColumnFamilyHandle], *args: Any, **kwargs: Any) -> List[Any]: ...
    def snapshot(self) -> "Snapshot": ...
    def get_property(self, prop: bytes, column_family: Optional[ColumnFamilyHandle] = None) -> Optional[bytes]: ...
    def get_live_files_metadata(self) -> List[Dict[str, Union[str, int, bytes]]]: ...
    def get_column_family_meta_data(self, column_family: Optional[ColumnFamilyHandle] = None) -> Dict[str, int]: ...
    def compact_range(
        self,
        begin: Optional[bytes] = None,
        end: Optional[bytes] = None,
        column_family: Optional[ColumnFamilyHandle] = None,
        **py_options: Any,
    ) -> None: ...
    @staticmethod
    def __parse_read_opts(
        verify_checksums: bool = False,
        fill_cache: bool = True,
        snapshot: Optional["Snapshot"] = None,
        read_tier: str = "all",
        total_order_seek: bool = False,
        iterate_lower_bound: Optional[bytes] = None,
        iterate_upper_bound: Optional[bytes] = None,
    ) -> Dict[str, Union[bool, Optional[bytes], Optional["Snapshot"]]]: ...
    @property
    def options(self) -> Optional[Options]: ...
    def create_column_family(self, name: bytes, copts: ColumnFamilyOptions) -> ColumnFamilyHandle: ...
    def drop_column_family(self, weak_handle: ColumnFamilyHandle) -> None: ...

def repair_db(db_name: str, opts: Options) -> None: ...
def list_column_families(db_name: str, opts: Options) -> List[bytes]: ...

class TransactionDB(DB):
    tdb_opts: TransactionDBOptions

    def __init__(
        self,
        db_name: str,
        opts: Options,
        column_families: Optional[Dict[bytes, ColumnFamilyOptions]] = None,
        tdb_opts: Optional[TransactionDBOptions] = None,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    @property
    def transaction_options(self) -> Optional[TransactionDBOptions]: ...
    def close(self, safe: bool = True) -> None: ...
