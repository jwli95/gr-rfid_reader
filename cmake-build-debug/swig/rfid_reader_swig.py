# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_rfid_reader_swig', [dirname(__file__)])
        except ImportError:
            import _rfid_reader_swig
            return _rfid_reader_swig
        if fp is not None:
            try:
                _mod = imp.load_module('_rfid_reader_swig', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _rfid_reader_swig = swig_import_helper()
    del swig_import_helper
else:
    import _rfid_reader_swig
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr



def high_res_timer_now():
    """high_res_timer_now() -> gr::high_res_timer_type"""
    return _rfid_reader_swig.high_res_timer_now()

def high_res_timer_now_perfmon():
    """high_res_timer_now_perfmon() -> gr::high_res_timer_type"""
    return _rfid_reader_swig.high_res_timer_now_perfmon()

def high_res_timer_tps():
    """high_res_timer_tps() -> gr::high_res_timer_type"""
    return _rfid_reader_swig.high_res_timer_tps()

def high_res_timer_epoch():
    """high_res_timer_epoch() -> gr::high_res_timer_type"""
    return _rfid_reader_swig.high_res_timer_epoch()
class reader(object):
    """
    <+description of block+>

    Constructor Specific Documentation:

    Return a shared_ptr to a new instance of rfid_reader::reader.

    To avoid accidental use of raw pointers, rfid_reader::reader's constructor is in a private implementation class. rfid_reader::reader::make is the public interface for creating new instances.

    Args:
        dac_rate : 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def make(dac_rate):
        """
        make(int dac_rate) -> reader_sptr

        <+description of block+>

        Constructor Specific Documentation:

        Return a shared_ptr to a new instance of rfid_reader::reader.

        To avoid accidental use of raw pointers, rfid_reader::reader's constructor is in a private implementation class. rfid_reader::reader::make is the public interface for creating new instances.

        Args:
            dac_rate : 
        """
        return _rfid_reader_swig.reader_make(dac_rate)

    make = staticmethod(make)
    __swig_destroy__ = _rfid_reader_swig.delete_reader
    __del__ = lambda self: None
reader_swigregister = _rfid_reader_swig.reader_swigregister
reader_swigregister(reader)

def reader_make(dac_rate):
    """
    reader_make(int dac_rate) -> reader_sptr

    <+description of block+>

    Constructor Specific Documentation:

    Return a shared_ptr to a new instance of rfid_reader::reader.

    To avoid accidental use of raw pointers, rfid_reader::reader's constructor is in a private implementation class. rfid_reader::reader::make is the public interface for creating new instances.

    Args:
        dac_rate : 
    """
    return _rfid_reader_swig.reader_make(dac_rate)

class reader_sptr(object):
    """Proxy of C++ boost::shared_ptr<(gr::rfid_reader::reader)> class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(boost::shared_ptr<(gr::rfid_reader::reader)> self) -> reader_sptr
        __init__(boost::shared_ptr<(gr::rfid_reader::reader)> self, reader p) -> reader_sptr
        """
        this = _rfid_reader_swig.new_reader_sptr(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def __deref__(self):
        """__deref__(reader_sptr self) -> reader"""
        return _rfid_reader_swig.reader_sptr___deref__(self)

    __swig_destroy__ = _rfid_reader_swig.delete_reader_sptr
    __del__ = lambda self: None

    def make(self, dac_rate):
        """
        make(reader_sptr self, int dac_rate) -> reader_sptr

        <+description of block+>

        Constructor Specific Documentation:

        Return a shared_ptr to a new instance of rfid_reader::reader.

        To avoid accidental use of raw pointers, rfid_reader::reader's constructor is in a private implementation class. rfid_reader::reader::make is the public interface for creating new instances.

        Args:
            dac_rate : 
        """
        return _rfid_reader_swig.reader_sptr_make(self, dac_rate)


    def history(self):
        """history(reader_sptr self) -> unsigned int"""
        return _rfid_reader_swig.reader_sptr_history(self)


    def declare_sample_delay(self, *args):
        """
        declare_sample_delay(reader_sptr self, int which, int delay)
        declare_sample_delay(reader_sptr self, unsigned int delay)
        """
        return _rfid_reader_swig.reader_sptr_declare_sample_delay(self, *args)


    def sample_delay(self, which):
        """sample_delay(reader_sptr self, int which) -> unsigned int"""
        return _rfid_reader_swig.reader_sptr_sample_delay(self, which)


    def output_multiple(self):
        """output_multiple(reader_sptr self) -> int"""
        return _rfid_reader_swig.reader_sptr_output_multiple(self)


    def relative_rate(self):
        """relative_rate(reader_sptr self) -> double"""
        return _rfid_reader_swig.reader_sptr_relative_rate(self)


    def start(self):
        """start(reader_sptr self) -> bool"""
        return _rfid_reader_swig.reader_sptr_start(self)


    def stop(self):
        """stop(reader_sptr self) -> bool"""
        return _rfid_reader_swig.reader_sptr_stop(self)


    def nitems_read(self, which_input):
        """nitems_read(reader_sptr self, unsigned int which_input) -> uint64_t"""
        return _rfid_reader_swig.reader_sptr_nitems_read(self, which_input)


    def nitems_written(self, which_output):
        """nitems_written(reader_sptr self, unsigned int which_output) -> uint64_t"""
        return _rfid_reader_swig.reader_sptr_nitems_written(self, which_output)


    def max_noutput_items(self):
        """max_noutput_items(reader_sptr self) -> int"""
        return _rfid_reader_swig.reader_sptr_max_noutput_items(self)


    def set_max_noutput_items(self, m):
        """set_max_noutput_items(reader_sptr self, int m)"""
        return _rfid_reader_swig.reader_sptr_set_max_noutput_items(self, m)


    def unset_max_noutput_items(self):
        """unset_max_noutput_items(reader_sptr self)"""
        return _rfid_reader_swig.reader_sptr_unset_max_noutput_items(self)


    def is_set_max_noutput_items(self):
        """is_set_max_noutput_items(reader_sptr self) -> bool"""
        return _rfid_reader_swig.reader_sptr_is_set_max_noutput_items(self)


    def set_min_noutput_items(self, m):
        """set_min_noutput_items(reader_sptr self, int m)"""
        return _rfid_reader_swig.reader_sptr_set_min_noutput_items(self, m)


    def min_noutput_items(self):
        """min_noutput_items(reader_sptr self) -> int"""
        return _rfid_reader_swig.reader_sptr_min_noutput_items(self)


    def max_output_buffer(self, i):
        """max_output_buffer(reader_sptr self, int i) -> long"""
        return _rfid_reader_swig.reader_sptr_max_output_buffer(self, i)


    def set_max_output_buffer(self, *args):
        """
        set_max_output_buffer(reader_sptr self, long max_output_buffer)
        set_max_output_buffer(reader_sptr self, int port, long max_output_buffer)
        """
        return _rfid_reader_swig.reader_sptr_set_max_output_buffer(self, *args)


    def min_output_buffer(self, i):
        """min_output_buffer(reader_sptr self, int i) -> long"""
        return _rfid_reader_swig.reader_sptr_min_output_buffer(self, i)


    def set_min_output_buffer(self, *args):
        """
        set_min_output_buffer(reader_sptr self, long min_output_buffer)
        set_min_output_buffer(reader_sptr self, int port, long min_output_buffer)
        """
        return _rfid_reader_swig.reader_sptr_set_min_output_buffer(self, *args)


    def pc_noutput_items(self):
        """pc_noutput_items(reader_sptr self) -> float"""
        return _rfid_reader_swig.reader_sptr_pc_noutput_items(self)


    def pc_noutput_items_avg(self):
        """pc_noutput_items_avg(reader_sptr self) -> float"""
        return _rfid_reader_swig.reader_sptr_pc_noutput_items_avg(self)


    def pc_noutput_items_var(self):
        """pc_noutput_items_var(reader_sptr self) -> float"""
        return _rfid_reader_swig.reader_sptr_pc_noutput_items_var(self)


    def pc_nproduced(self):
        """pc_nproduced(reader_sptr self) -> float"""
        return _rfid_reader_swig.reader_sptr_pc_nproduced(self)


    def pc_nproduced_avg(self):
        """pc_nproduced_avg(reader_sptr self) -> float"""
        return _rfid_reader_swig.reader_sptr_pc_nproduced_avg(self)


    def pc_nproduced_var(self):
        """pc_nproduced_var(reader_sptr self) -> float"""
        return _rfid_reader_swig.reader_sptr_pc_nproduced_var(self)


    def pc_input_buffers_full(self, *args):
        """
        pc_input_buffers_full(reader_sptr self, int which) -> float
        pc_input_buffers_full(reader_sptr self) -> pmt_vector_float
        """
        return _rfid_reader_swig.reader_sptr_pc_input_buffers_full(self, *args)


    def pc_input_buffers_full_avg(self, *args):
        """
        pc_input_buffers_full_avg(reader_sptr self, int which) -> float
        pc_input_buffers_full_avg(reader_sptr self) -> pmt_vector_float
        """
        return _rfid_reader_swig.reader_sptr_pc_input_buffers_full_avg(self, *args)


    def pc_input_buffers_full_var(self, *args):
        """
        pc_input_buffers_full_var(reader_sptr self, int which) -> float
        pc_input_buffers_full_var(reader_sptr self) -> pmt_vector_float
        """
        return _rfid_reader_swig.reader_sptr_pc_input_buffers_full_var(self, *args)


    def pc_output_buffers_full(self, *args):
        """
        pc_output_buffers_full(reader_sptr self, int which) -> float
        pc_output_buffers_full(reader_sptr self) -> pmt_vector_float
        """
        return _rfid_reader_swig.reader_sptr_pc_output_buffers_full(self, *args)


    def pc_output_buffers_full_avg(self, *args):
        """
        pc_output_buffers_full_avg(reader_sptr self, int which) -> float
        pc_output_buffers_full_avg(reader_sptr self) -> pmt_vector_float
        """
        return _rfid_reader_swig.reader_sptr_pc_output_buffers_full_avg(self, *args)


    def pc_output_buffers_full_var(self, *args):
        """
        pc_output_buffers_full_var(reader_sptr self, int which) -> float
        pc_output_buffers_full_var(reader_sptr self) -> pmt_vector_float
        """
        return _rfid_reader_swig.reader_sptr_pc_output_buffers_full_var(self, *args)


    def pc_work_time(self):
        """pc_work_time(reader_sptr self) -> float"""
        return _rfid_reader_swig.reader_sptr_pc_work_time(self)


    def pc_work_time_avg(self):
        """pc_work_time_avg(reader_sptr self) -> float"""
        return _rfid_reader_swig.reader_sptr_pc_work_time_avg(self)


    def pc_work_time_var(self):
        """pc_work_time_var(reader_sptr self) -> float"""
        return _rfid_reader_swig.reader_sptr_pc_work_time_var(self)


    def pc_work_time_total(self):
        """pc_work_time_total(reader_sptr self) -> float"""
        return _rfid_reader_swig.reader_sptr_pc_work_time_total(self)


    def pc_throughput_avg(self):
        """pc_throughput_avg(reader_sptr self) -> float"""
        return _rfid_reader_swig.reader_sptr_pc_throughput_avg(self)


    def set_processor_affinity(self, mask):
        """set_processor_affinity(reader_sptr self, std::vector< int,std::allocator< int > > const & mask)"""
        return _rfid_reader_swig.reader_sptr_set_processor_affinity(self, mask)


    def unset_processor_affinity(self):
        """unset_processor_affinity(reader_sptr self)"""
        return _rfid_reader_swig.reader_sptr_unset_processor_affinity(self)


    def processor_affinity(self):
        """processor_affinity(reader_sptr self) -> std::vector< int,std::allocator< int > >"""
        return _rfid_reader_swig.reader_sptr_processor_affinity(self)


    def active_thread_priority(self):
        """active_thread_priority(reader_sptr self) -> int"""
        return _rfid_reader_swig.reader_sptr_active_thread_priority(self)


    def thread_priority(self):
        """thread_priority(reader_sptr self) -> int"""
        return _rfid_reader_swig.reader_sptr_thread_priority(self)


    def set_thread_priority(self, priority):
        """set_thread_priority(reader_sptr self, int priority) -> int"""
        return _rfid_reader_swig.reader_sptr_set_thread_priority(self, priority)


    def name(self):
        """name(reader_sptr self) -> std::string"""
        return _rfid_reader_swig.reader_sptr_name(self)


    def symbol_name(self):
        """symbol_name(reader_sptr self) -> std::string"""
        return _rfid_reader_swig.reader_sptr_symbol_name(self)


    def input_signature(self):
        """input_signature(reader_sptr self) -> io_signature_sptr"""
        return _rfid_reader_swig.reader_sptr_input_signature(self)


    def output_signature(self):
        """output_signature(reader_sptr self) -> io_signature_sptr"""
        return _rfid_reader_swig.reader_sptr_output_signature(self)


    def unique_id(self):
        """unique_id(reader_sptr self) -> long"""
        return _rfid_reader_swig.reader_sptr_unique_id(self)


    def to_basic_block(self):
        """to_basic_block(reader_sptr self) -> basic_block_sptr"""
        return _rfid_reader_swig.reader_sptr_to_basic_block(self)


    def check_topology(self, ninputs, noutputs):
        """check_topology(reader_sptr self, int ninputs, int noutputs) -> bool"""
        return _rfid_reader_swig.reader_sptr_check_topology(self, ninputs, noutputs)


    def alias(self):
        """alias(reader_sptr self) -> std::string"""
        return _rfid_reader_swig.reader_sptr_alias(self)


    def set_block_alias(self, name):
        """set_block_alias(reader_sptr self, std::string name)"""
        return _rfid_reader_swig.reader_sptr_set_block_alias(self, name)


    def _post(self, which_port, msg):
        """_post(reader_sptr self, swig_int_ptr which_port, swig_int_ptr msg)"""
        return _rfid_reader_swig.reader_sptr__post(self, which_port, msg)


    def message_ports_in(self):
        """message_ports_in(reader_sptr self) -> swig_int_ptr"""
        return _rfid_reader_swig.reader_sptr_message_ports_in(self)


    def message_ports_out(self):
        """message_ports_out(reader_sptr self) -> swig_int_ptr"""
        return _rfid_reader_swig.reader_sptr_message_ports_out(self)


    def message_subscribers(self, which_port):
        """message_subscribers(reader_sptr self, swig_int_ptr which_port) -> swig_int_ptr"""
        return _rfid_reader_swig.reader_sptr_message_subscribers(self, which_port)

reader_sptr_swigregister = _rfid_reader_swig.reader_sptr_swigregister
reader_sptr_swigregister(reader_sptr)


reader_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id())
reader = reader.make;


_rfid_reader_swig.RUNNING_swigconstant(_rfid_reader_swig)
RUNNING = _rfid_reader_swig.RUNNING

_rfid_reader_swig.TERMINATED_swigconstant(_rfid_reader_swig)
TERMINATED = _rfid_reader_swig.TERMINATED

_rfid_reader_swig.SEND_QUERY_swigconstant(_rfid_reader_swig)
SEND_QUERY = _rfid_reader_swig.SEND_QUERY

_rfid_reader_swig.SEND_ACK_swigconstant(_rfid_reader_swig)
SEND_ACK = _rfid_reader_swig.SEND_ACK

_rfid_reader_swig.SEND_QUERY_REP_swigconstant(_rfid_reader_swig)
SEND_QUERY_REP = _rfid_reader_swig.SEND_QUERY_REP

_rfid_reader_swig.IDLE_swigconstant(_rfid_reader_swig)
IDLE = _rfid_reader_swig.IDLE

_rfid_reader_swig.SEND_CW_swigconstant(_rfid_reader_swig)
SEND_CW = _rfid_reader_swig.SEND_CW

_rfid_reader_swig.START_swigconstant(_rfid_reader_swig)
START = _rfid_reader_swig.START

_rfid_reader_swig.SEND_QUERY_ADJUST_swigconstant(_rfid_reader_swig)
SEND_QUERY_ADJUST = _rfid_reader_swig.SEND_QUERY_ADJUST

_rfid_reader_swig.SEND_NAK_QR_swigconstant(_rfid_reader_swig)
SEND_NAK_QR = _rfid_reader_swig.SEND_NAK_QR

_rfid_reader_swig.SEND_NAK_Q_swigconstant(_rfid_reader_swig)
SEND_NAK_Q = _rfid_reader_swig.SEND_NAK_Q

_rfid_reader_swig.POWER_DOWN_swigconstant(_rfid_reader_swig)
POWER_DOWN = _rfid_reader_swig.POWER_DOWN

_rfid_reader_swig.GATE_OPEN_swigconstant(_rfid_reader_swig)
GATE_OPEN = _rfid_reader_swig.GATE_OPEN

_rfid_reader_swig.GATE_CLOSED_swigconstant(_rfid_reader_swig)
GATE_CLOSED = _rfid_reader_swig.GATE_CLOSED

_rfid_reader_swig.GATE_SEEK_RN16_swigconstant(_rfid_reader_swig)
GATE_SEEK_RN16 = _rfid_reader_swig.GATE_SEEK_RN16

_rfid_reader_swig.GATE_SEEK_EPC_swigconstant(_rfid_reader_swig)
GATE_SEEK_EPC = _rfid_reader_swig.GATE_SEEK_EPC

_rfid_reader_swig.DECODER_DECODE_RN16_swigconstant(_rfid_reader_swig)
DECODER_DECODE_RN16 = _rfid_reader_swig.DECODER_DECODE_RN16

_rfid_reader_swig.DECODER_DECODE_EPC_swigconstant(_rfid_reader_swig)
DECODER_DECODE_EPC = _rfid_reader_swig.DECODER_DECODE_EPC
class READER_STATS(object):
    """Proxy of C++ gr::rfid_reader::READER_STATS class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    n_queries_sent = _swig_property(_rfid_reader_swig.READER_STATS_n_queries_sent_get, _rfid_reader_swig.READER_STATS_n_queries_sent_set)
    cur_inventory_round = _swig_property(_rfid_reader_swig.READER_STATS_cur_inventory_round_get, _rfid_reader_swig.READER_STATS_cur_inventory_round_set)
    cur_slot_number = _swig_property(_rfid_reader_swig.READER_STATS_cur_slot_number_get, _rfid_reader_swig.READER_STATS_cur_slot_number_set)
    max_slot_number = _swig_property(_rfid_reader_swig.READER_STATS_max_slot_number_get, _rfid_reader_swig.READER_STATS_max_slot_number_set)
    max_inventory_round = _swig_property(_rfid_reader_swig.READER_STATS_max_inventory_round_get, _rfid_reader_swig.READER_STATS_max_inventory_round_set)
    n_epc_correct = _swig_property(_rfid_reader_swig.READER_STATS_n_epc_correct_get, _rfid_reader_swig.READER_STATS_n_epc_correct_set)
    unique_tags_round = _swig_property(_rfid_reader_swig.READER_STATS_unique_tags_round_get, _rfid_reader_swig.READER_STATS_unique_tags_round_set)
    tag_reads = _swig_property(_rfid_reader_swig.READER_STATS_tag_reads_get, _rfid_reader_swig.READER_STATS_tag_reads_set)
    start = _swig_property(_rfid_reader_swig.READER_STATS_start_get, _rfid_reader_swig.READER_STATS_start_set)
    end = _swig_property(_rfid_reader_swig.READER_STATS_end_get, _rfid_reader_swig.READER_STATS_end_set)

    def __init__(self):
        """__init__(gr::rfid_reader::READER_STATS self) -> READER_STATS"""
        this = _rfid_reader_swig.new_READER_STATS()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _rfid_reader_swig.delete_READER_STATS
    __del__ = lambda self: None
READER_STATS_swigregister = _rfid_reader_swig.READER_STATS_swigregister
READER_STATS_swigregister(READER_STATS)

class READER_STATE(object):
    """Proxy of C++ gr::rfid_reader::READER_STATE class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    status = _swig_property(_rfid_reader_swig.READER_STATE_status_get, _rfid_reader_swig.READER_STATE_status_set)
    gen2_logic_status = _swig_property(_rfid_reader_swig.READER_STATE_gen2_logic_status_get, _rfid_reader_swig.READER_STATE_gen2_logic_status_set)
    gate_status = _swig_property(_rfid_reader_swig.READER_STATE_gate_status_get, _rfid_reader_swig.READER_STATE_gate_status_set)
    decoder_status = _swig_property(_rfid_reader_swig.READER_STATE_decoder_status_get, _rfid_reader_swig.READER_STATE_decoder_status_set)
    reader_stats = _swig_property(_rfid_reader_swig.READER_STATE_reader_stats_get, _rfid_reader_swig.READER_STATE_reader_stats_set)
    magn_squared_samples = _swig_property(_rfid_reader_swig.READER_STATE_magn_squared_samples_get, _rfid_reader_swig.READER_STATE_magn_squared_samples_set)
    n_samples_to_ungate = _swig_property(_rfid_reader_swig.READER_STATE_n_samples_to_ungate_get, _rfid_reader_swig.READER_STATE_n_samples_to_ungate_set)

    def __init__(self):
        """__init__(gr::rfid_reader::READER_STATE self) -> READER_STATE"""
        this = _rfid_reader_swig.new_READER_STATE()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _rfid_reader_swig.delete_READER_STATE
    __del__ = lambda self: None
READER_STATE_swigregister = _rfid_reader_swig.READER_STATE_swigregister
READER_STATE_swigregister(READER_STATE)


def initialize_reader_state():
    """initialize_reader_state()"""
    return _rfid_reader_swig.initialize_reader_state()
class gate(object):
    """
    <+description of block+>

    Constructor Specific Documentation:

    Return a shared_ptr to a new instance of rfid_reader::gate.

    To avoid accidental use of raw pointers, rfid_reader::gate's constructor is in a private implementation class. rfid_reader::gate::make is the public interface for creating new instances.

    Args:
        sample_rate : 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def make(sample_rate):
        """
        make(int sample_rate) -> gate_sptr

        <+description of block+>

        Constructor Specific Documentation:

        Return a shared_ptr to a new instance of rfid_reader::gate.

        To avoid accidental use of raw pointers, rfid_reader::gate's constructor is in a private implementation class. rfid_reader::gate::make is the public interface for creating new instances.

        Args:
            sample_rate : 
        """
        return _rfid_reader_swig.gate_make(sample_rate)

    make = staticmethod(make)
    __swig_destroy__ = _rfid_reader_swig.delete_gate
    __del__ = lambda self: None
gate_swigregister = _rfid_reader_swig.gate_swigregister
gate_swigregister(gate)
cvar = _rfid_reader_swig.cvar
FIXED_Q = cvar.FIXED_Q
MAX_NUM_QUERIES = cvar.MAX_NUM_QUERIES
Q_VALUE = cvar.Q_VALUE
P_DOWN = cvar.P_DOWN
CW_D = cvar.CW_D
P_DOWN_D = cvar.P_DOWN_D
T1_D = cvar.T1_D
T2_D = cvar.T2_D
PW_D = cvar.PW_D
DELIM_D = cvar.DELIM_D
TRCAL_D = cvar.TRCAL_D
RTCAL_D = cvar.RTCAL_D
NUM_PULSES_COMMAND = cvar.NUM_PULSES_COMMAND
NUMBER_UNIQUE_TAGS = cvar.NUMBER_UNIQUE_TAGS
PILOT_TONE = cvar.PILOT_TONE
TAG_PREAMBLE_BITS = cvar.TAG_PREAMBLE_BITS
RN16_BITS = cvar.RN16_BITS
EPC_BITS = cvar.EPC_BITS
QUERY_LENGTH = cvar.QUERY_LENGTH
T_READER_FREQ = cvar.T_READER_FREQ
TAG_BIT_D = cvar.TAG_BIT_D
RN16_D = cvar.RN16_D
EPC_D = cvar.EPC_D
QUERY_CODE = cvar.QUERY_CODE
M = cvar.M
SEL = cvar.SEL
SESSION = cvar.SESSION
TARGET = cvar.TARGET
TREXT = cvar.TREXT
DR = cvar.DR
NAK_CODE = cvar.NAK_CODE
ACK_CODE = cvar.ACK_CODE
QADJ_CODE = cvar.QADJ_CODE
Q_UPDN = cvar.Q_UPDN
TAG_PREAMBLE = cvar.TAG_PREAMBLE
THRESH_FRACTION = cvar.THRESH_FRACTION
WIN_SIZE_D = cvar.WIN_SIZE_D
DC_SIZE_D = cvar.DC_SIZE_D

def gate_make(sample_rate):
    """
    gate_make(int sample_rate) -> gate_sptr

    <+description of block+>

    Constructor Specific Documentation:

    Return a shared_ptr to a new instance of rfid_reader::gate.

    To avoid accidental use of raw pointers, rfid_reader::gate's constructor is in a private implementation class. rfid_reader::gate::make is the public interface for creating new instances.

    Args:
        sample_rate : 
    """
    return _rfid_reader_swig.gate_make(sample_rate)

class gate_sptr(object):
    """Proxy of C++ boost::shared_ptr<(gr::rfid_reader::gate)> class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(boost::shared_ptr<(gr::rfid_reader::gate)> self) -> gate_sptr
        __init__(boost::shared_ptr<(gr::rfid_reader::gate)> self, gate p) -> gate_sptr
        """
        this = _rfid_reader_swig.new_gate_sptr(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def __deref__(self):
        """__deref__(gate_sptr self) -> gate"""
        return _rfid_reader_swig.gate_sptr___deref__(self)

    __swig_destroy__ = _rfid_reader_swig.delete_gate_sptr
    __del__ = lambda self: None

    def make(self, sample_rate):
        """
        make(gate_sptr self, int sample_rate) -> gate_sptr

        <+description of block+>

        Constructor Specific Documentation:

        Return a shared_ptr to a new instance of rfid_reader::gate.

        To avoid accidental use of raw pointers, rfid_reader::gate's constructor is in a private implementation class. rfid_reader::gate::make is the public interface for creating new instances.

        Args:
            sample_rate : 
        """
        return _rfid_reader_swig.gate_sptr_make(self, sample_rate)


    def history(self):
        """history(gate_sptr self) -> unsigned int"""
        return _rfid_reader_swig.gate_sptr_history(self)


    def declare_sample_delay(self, *args):
        """
        declare_sample_delay(gate_sptr self, int which, int delay)
        declare_sample_delay(gate_sptr self, unsigned int delay)
        """
        return _rfid_reader_swig.gate_sptr_declare_sample_delay(self, *args)


    def sample_delay(self, which):
        """sample_delay(gate_sptr self, int which) -> unsigned int"""
        return _rfid_reader_swig.gate_sptr_sample_delay(self, which)


    def output_multiple(self):
        """output_multiple(gate_sptr self) -> int"""
        return _rfid_reader_swig.gate_sptr_output_multiple(self)


    def relative_rate(self):
        """relative_rate(gate_sptr self) -> double"""
        return _rfid_reader_swig.gate_sptr_relative_rate(self)


    def start(self):
        """start(gate_sptr self) -> bool"""
        return _rfid_reader_swig.gate_sptr_start(self)


    def stop(self):
        """stop(gate_sptr self) -> bool"""
        return _rfid_reader_swig.gate_sptr_stop(self)


    def nitems_read(self, which_input):
        """nitems_read(gate_sptr self, unsigned int which_input) -> uint64_t"""
        return _rfid_reader_swig.gate_sptr_nitems_read(self, which_input)


    def nitems_written(self, which_output):
        """nitems_written(gate_sptr self, unsigned int which_output) -> uint64_t"""
        return _rfid_reader_swig.gate_sptr_nitems_written(self, which_output)


    def max_noutput_items(self):
        """max_noutput_items(gate_sptr self) -> int"""
        return _rfid_reader_swig.gate_sptr_max_noutput_items(self)


    def set_max_noutput_items(self, m):
        """set_max_noutput_items(gate_sptr self, int m)"""
        return _rfid_reader_swig.gate_sptr_set_max_noutput_items(self, m)


    def unset_max_noutput_items(self):
        """unset_max_noutput_items(gate_sptr self)"""
        return _rfid_reader_swig.gate_sptr_unset_max_noutput_items(self)


    def is_set_max_noutput_items(self):
        """is_set_max_noutput_items(gate_sptr self) -> bool"""
        return _rfid_reader_swig.gate_sptr_is_set_max_noutput_items(self)


    def set_min_noutput_items(self, m):
        """set_min_noutput_items(gate_sptr self, int m)"""
        return _rfid_reader_swig.gate_sptr_set_min_noutput_items(self, m)


    def min_noutput_items(self):
        """min_noutput_items(gate_sptr self) -> int"""
        return _rfid_reader_swig.gate_sptr_min_noutput_items(self)


    def max_output_buffer(self, i):
        """max_output_buffer(gate_sptr self, int i) -> long"""
        return _rfid_reader_swig.gate_sptr_max_output_buffer(self, i)


    def set_max_output_buffer(self, *args):
        """
        set_max_output_buffer(gate_sptr self, long max_output_buffer)
        set_max_output_buffer(gate_sptr self, int port, long max_output_buffer)
        """
        return _rfid_reader_swig.gate_sptr_set_max_output_buffer(self, *args)


    def min_output_buffer(self, i):
        """min_output_buffer(gate_sptr self, int i) -> long"""
        return _rfid_reader_swig.gate_sptr_min_output_buffer(self, i)


    def set_min_output_buffer(self, *args):
        """
        set_min_output_buffer(gate_sptr self, long min_output_buffer)
        set_min_output_buffer(gate_sptr self, int port, long min_output_buffer)
        """
        return _rfid_reader_swig.gate_sptr_set_min_output_buffer(self, *args)


    def pc_noutput_items(self):
        """pc_noutput_items(gate_sptr self) -> float"""
        return _rfid_reader_swig.gate_sptr_pc_noutput_items(self)


    def pc_noutput_items_avg(self):
        """pc_noutput_items_avg(gate_sptr self) -> float"""
        return _rfid_reader_swig.gate_sptr_pc_noutput_items_avg(self)


    def pc_noutput_items_var(self):
        """pc_noutput_items_var(gate_sptr self) -> float"""
        return _rfid_reader_swig.gate_sptr_pc_noutput_items_var(self)


    def pc_nproduced(self):
        """pc_nproduced(gate_sptr self) -> float"""
        return _rfid_reader_swig.gate_sptr_pc_nproduced(self)


    def pc_nproduced_avg(self):
        """pc_nproduced_avg(gate_sptr self) -> float"""
        return _rfid_reader_swig.gate_sptr_pc_nproduced_avg(self)


    def pc_nproduced_var(self):
        """pc_nproduced_var(gate_sptr self) -> float"""
        return _rfid_reader_swig.gate_sptr_pc_nproduced_var(self)


    def pc_input_buffers_full(self, *args):
        """
        pc_input_buffers_full(gate_sptr self, int which) -> float
        pc_input_buffers_full(gate_sptr self) -> pmt_vector_float
        """
        return _rfid_reader_swig.gate_sptr_pc_input_buffers_full(self, *args)


    def pc_input_buffers_full_avg(self, *args):
        """
        pc_input_buffers_full_avg(gate_sptr self, int which) -> float
        pc_input_buffers_full_avg(gate_sptr self) -> pmt_vector_float
        """
        return _rfid_reader_swig.gate_sptr_pc_input_buffers_full_avg(self, *args)


    def pc_input_buffers_full_var(self, *args):
        """
        pc_input_buffers_full_var(gate_sptr self, int which) -> float
        pc_input_buffers_full_var(gate_sptr self) -> pmt_vector_float
        """
        return _rfid_reader_swig.gate_sptr_pc_input_buffers_full_var(self, *args)


    def pc_output_buffers_full(self, *args):
        """
        pc_output_buffers_full(gate_sptr self, int which) -> float
        pc_output_buffers_full(gate_sptr self) -> pmt_vector_float
        """
        return _rfid_reader_swig.gate_sptr_pc_output_buffers_full(self, *args)


    def pc_output_buffers_full_avg(self, *args):
        """
        pc_output_buffers_full_avg(gate_sptr self, int which) -> float
        pc_output_buffers_full_avg(gate_sptr self) -> pmt_vector_float
        """
        return _rfid_reader_swig.gate_sptr_pc_output_buffers_full_avg(self, *args)


    def pc_output_buffers_full_var(self, *args):
        """
        pc_output_buffers_full_var(gate_sptr self, int which) -> float
        pc_output_buffers_full_var(gate_sptr self) -> pmt_vector_float
        """
        return _rfid_reader_swig.gate_sptr_pc_output_buffers_full_var(self, *args)


    def pc_work_time(self):
        """pc_work_time(gate_sptr self) -> float"""
        return _rfid_reader_swig.gate_sptr_pc_work_time(self)


    def pc_work_time_avg(self):
        """pc_work_time_avg(gate_sptr self) -> float"""
        return _rfid_reader_swig.gate_sptr_pc_work_time_avg(self)


    def pc_work_time_var(self):
        """pc_work_time_var(gate_sptr self) -> float"""
        return _rfid_reader_swig.gate_sptr_pc_work_time_var(self)


    def pc_work_time_total(self):
        """pc_work_time_total(gate_sptr self) -> float"""
        return _rfid_reader_swig.gate_sptr_pc_work_time_total(self)


    def pc_throughput_avg(self):
        """pc_throughput_avg(gate_sptr self) -> float"""
        return _rfid_reader_swig.gate_sptr_pc_throughput_avg(self)


    def set_processor_affinity(self, mask):
        """set_processor_affinity(gate_sptr self, std::vector< int,std::allocator< int > > const & mask)"""
        return _rfid_reader_swig.gate_sptr_set_processor_affinity(self, mask)


    def unset_processor_affinity(self):
        """unset_processor_affinity(gate_sptr self)"""
        return _rfid_reader_swig.gate_sptr_unset_processor_affinity(self)


    def processor_affinity(self):
        """processor_affinity(gate_sptr self) -> std::vector< int,std::allocator< int > >"""
        return _rfid_reader_swig.gate_sptr_processor_affinity(self)


    def active_thread_priority(self):
        """active_thread_priority(gate_sptr self) -> int"""
        return _rfid_reader_swig.gate_sptr_active_thread_priority(self)


    def thread_priority(self):
        """thread_priority(gate_sptr self) -> int"""
        return _rfid_reader_swig.gate_sptr_thread_priority(self)


    def set_thread_priority(self, priority):
        """set_thread_priority(gate_sptr self, int priority) -> int"""
        return _rfid_reader_swig.gate_sptr_set_thread_priority(self, priority)


    def name(self):
        """name(gate_sptr self) -> std::string"""
        return _rfid_reader_swig.gate_sptr_name(self)


    def symbol_name(self):
        """symbol_name(gate_sptr self) -> std::string"""
        return _rfid_reader_swig.gate_sptr_symbol_name(self)


    def input_signature(self):
        """input_signature(gate_sptr self) -> io_signature_sptr"""
        return _rfid_reader_swig.gate_sptr_input_signature(self)


    def output_signature(self):
        """output_signature(gate_sptr self) -> io_signature_sptr"""
        return _rfid_reader_swig.gate_sptr_output_signature(self)


    def unique_id(self):
        """unique_id(gate_sptr self) -> long"""
        return _rfid_reader_swig.gate_sptr_unique_id(self)


    def to_basic_block(self):
        """to_basic_block(gate_sptr self) -> basic_block_sptr"""
        return _rfid_reader_swig.gate_sptr_to_basic_block(self)


    def check_topology(self, ninputs, noutputs):
        """check_topology(gate_sptr self, int ninputs, int noutputs) -> bool"""
        return _rfid_reader_swig.gate_sptr_check_topology(self, ninputs, noutputs)


    def alias(self):
        """alias(gate_sptr self) -> std::string"""
        return _rfid_reader_swig.gate_sptr_alias(self)


    def set_block_alias(self, name):
        """set_block_alias(gate_sptr self, std::string name)"""
        return _rfid_reader_swig.gate_sptr_set_block_alias(self, name)


    def _post(self, which_port, msg):
        """_post(gate_sptr self, swig_int_ptr which_port, swig_int_ptr msg)"""
        return _rfid_reader_swig.gate_sptr__post(self, which_port, msg)


    def message_ports_in(self):
        """message_ports_in(gate_sptr self) -> swig_int_ptr"""
        return _rfid_reader_swig.gate_sptr_message_ports_in(self)


    def message_ports_out(self):
        """message_ports_out(gate_sptr self) -> swig_int_ptr"""
        return _rfid_reader_swig.gate_sptr_message_ports_out(self)


    def message_subscribers(self, which_port):
        """message_subscribers(gate_sptr self, swig_int_ptr which_port) -> swig_int_ptr"""
        return _rfid_reader_swig.gate_sptr_message_subscribers(self, which_port)

gate_sptr_swigregister = _rfid_reader_swig.gate_sptr_swigregister
gate_sptr_swigregister(gate_sptr)


gate_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id())
gate = gate.make;



