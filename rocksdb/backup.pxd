from libcpp cimport bool as cpp_bool
from libcpp.string cimport string
from libcpp.vector cimport vector
from libc.stdint cimport uint32_t
from libc.stdint cimport int64_t
from libc.stdint cimport uint64_t

from .status cimport Status
from .db cimport DB
from .env cimport Env

# TODO: For rocksdb >= 6.21.0, change to `rocksdb/utilities/backup_engine.h`.
cdef extern from "rocksdb/utilities/backup_engine.h" namespace "rocksdb":
    ctypedef uint32_t BackupID

    # TODO: For rocksdb >= 6.21.0, rename to `BackupEngineOptions`.
    cdef cppclass BackupEngineOptions:
        BackupEngineOptions(const string& backup_dir)

    cdef struct BackupInfo:
        BackupID backup_id
        int64_t timestamp
        uint64_t size

    cdef cppclass BackupEngine:
        Status CreateNewBackup(DB*, cpp_bool) except+ nogil
        Status PurgeOldBackups(uint32_t) except+ nogil
        Status DeleteBackup(BackupID) except+ nogil
        void StopBackup() except+ nogil
        void GetBackupInfo(vector[BackupInfo]*) except+ nogil
        Status RestoreDBFromBackup(BackupID, string&, string&) except+ nogil
        Status RestoreDBFromLatestBackup(string&, string&) except+ nogil

    # TODO: For rocksdb >= 6.21.0, swap order of first two parameters.
    cdef Status BackupEngine_Open "rocksdb::BackupEngine::Open"(
            Env*,
            BackupEngineOptions&,
            BackupEngine**)
