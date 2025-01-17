import lfigw.waveform_generator as wfg

wfd = wfg.WaveformDataset(spins_aligned=False, domain='RB',
                          extrinsic_at_train=True)

wfd.Nrb = 600
wfd.approximant = 'IMRPhenomPv2'

wfd.load_event('data/events/GW150914/', randpsd=True, randpsd_events=['GW150914', 'GW151012'])

wfd.importance_sampling = 'uniform_distance'

wfd.prior['distance'] = [100.0, 2000.0]
wfd.prior['a_1'][1] = 0.88
wfd.prior['a_2'][1] = 0.88

print('Dataset properties')
print('Event', wfd.event)
print(wfd.prior)
print('f_min', wfd.f_min)
print('f_min_psd', wfd.f_min_psd)
print('f_max', wfd.f_max)
print('delta_f', wfd.delta_f)
print('T', wfd.time_duration)
print('reference time', wfd.ref_time)

input('continue?')
wfd.generate_reduced_basis(1000000)
input('generate reduced basis have finished! continue?')
wfd.generate_dataset(5000000)

wfd.generate_noisy_test_data(5000)

wfd.save('waveforms/O1_randpsd')
wfd.save_train('waveforms/O1_randpsd')
wfd.save_noisy_test_data('waveforms/O1_randpsd')

print('Program complete. Waveform dataset has been saved.')
