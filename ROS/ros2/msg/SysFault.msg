# DID_SYS_FAULT (2) - System fault information.
# The device broadcasts this automatically every 10s while a critical fault is
# latched, and once on request (which reports the cause of the last reset).

# Bit values of "status" (see eSysFaultStatus in data_sets.h).  Values are given
# in decimal here (.msg constants must be decimal); the hex value is in the comment.

# Reset cause / general status
uint32 STATUS_HARDWARE_RESET=0                          # 0x00000000  No fault - normal hardware reset
uint32 STATUS_USER_RESET=1                              # 0x00000001  Reset commanded by user
uint32 STATUS_ENABLE_BOOTLOADER=2                       # 0x00000002  Reset into bootloader

# General errors (status & MASK_GENERAL_ERROR)
uint32 STATUS_SOFT_RESET=16                             # 0x00000010
uint32 STATUS_FLASH_MIGRATION_EVENT=32                  # 0x00000020
uint32 STATUS_FLASH_MIGRATION_COMPLETED=64              # 0x00000040
uint32 STATUS_RTK_MISC_ERROR=128                        # 0x00000080
uint32 STATUS_MCUBOOT_SWAP_FAILURE=256                  # 0x00000100
uint32 MASK_GENERAL_ERROR=4294967280                    # 0xFFFFFFF0

# Critical errors (status & MASK_CRITICAL_ERROR), usually followed by a reset
uint32 STATUS_HARD_FAULT=65536                          # 0x00010000
uint32 STATUS_USAGE_FAULT=131072                        # 0x00020000
uint32 STATUS_MEM_MANAGE=262144                         # 0x00040000  (SYS_FAULT_STATUS_MEM_MANGE)
uint32 STATUS_BUS_FAULT=524288                          # 0x00080000
uint32 STATUS_MALLOC_FAILED=1048576                     # 0x00100000
uint32 STATUS_STACK_OVERFLOW=2097152                    # 0x00200000
uint32 STATUS_INVALID_CODE_OPERATION=4194304            # 0x00400000
uint32 STATUS_FLASH_MIGRATION_MARKER_UPDATED=8388608    # 0x00800000
uint32 STATUS_WATCHDOG_RESET=16777216                   # 0x01000000
uint32 STATUS_RTK_BUFFER_LIMIT=33554432                 # 0x02000000
uint32 STATUS_SENSOR_CALIBRATION=67108864               # 0x04000000
uint32 STATUS_HARDWARE_DETECTION=134217728              # 0x08000000
uint32 MASK_CRITICAL_ERROR=4294901760                   # 0xFFFF0000

std_msgs/Header header

uint32 status               # System fault status bit field (see STATUS_* constants above)
string status_hex           # "status" formatted as hex (e.g. "0x01000000"), for convenience
string status_str           # Names of the bits set in "status", comma separated, for convenience

uint32 g1_task              # Fault type at hard fault (RTOS task, see eImxRtosTask / eGpxRtosTask)
uint32 g2_file_num          # Multipurpose register - file number at fault
uint32 g3_line_num          # Multipurpose register - line number at fault
uint32 g4                   # Multipurpose register at time of fault
uint32 g5_lr                # Multipurpose register - link register value at time of fault
uint32 pc                   # Program counter value at time of fault
uint32 psr                  # Program status register value at time of fault
