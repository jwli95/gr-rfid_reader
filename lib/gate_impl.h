/* -*- c++ -*- */
/* 
 * Copyright 2019 Jiawei.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_RFID_READER_GATE_IMPL_H
#define INCLUDED_RFID_READER_GATE_IMPL_H

#include <rfid_reader/gate.h>
#include <vector>
#include "rfid_reader/global_vars.h"

namespace gr {
    namespace rfid_reader {

        class gate_impl : public gate {
        private:
            // DEBUG
            bool tf;
            int tm;

            enum SIGNAL_STATE {NEG_EDGE, POS_EDGE};

            int   n_samples, n_samples_T1, n_samples_PW, n_samples_TAG_BIT;
            int  win_index, dc_index, win_length, dc_length, s_rate;
            float avg_ampl, num_pulses, sample_thresh;

            std::vector<float> win_samples,cw_samples;
            std::vector<gr_complex> dc_samples;
            gr_complex dc_est;

            SIGNAL_STATE signal_state;

        public:
            gate_impl(int sample_rate);

            ~gate_impl();

            // Where all the action really happens
            void forecast(int noutput_items, gr_vector_int &ninput_items_required);

            int general_work(int noutput_items,
                             gr_vector_int &ninput_items,
                             gr_vector_const_void_star &input_items,
                             gr_vector_void_star &output_items);
        };

    } // namespace rfid_reader
} // namespace gr

#endif /* INCLUDED_RFID_READER_GATE_IMPL_H */

