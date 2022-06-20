#!/usr/bin/env python
# coding: utf-8

from opentrons import protocol_api

metadata = {
    'protocolName': 'Antibodies Aliquoting (Multichannel pippete using single channel)',
    'apiLevel': '2.11',
    'author': 'Matt Zw & Javier Lomas'}

def run(ctx):
    # lights on
    #ctx.set_rail_lights(on=True)

    # Loading tipracks and pipette instrument
    tipracks = [ctx.load_labware('opentrons_96_tiprack_300ul', '4')]
    m300 = ctx.load_instrument('p300_multi_gen2', 'right')

    # Stable code to allow for multichannel to properly use only one channel - shouldn't edit

    per_tip_pickup_current = .1
    num_channels_per_pickup = 1  # (only pickup tips on front-most channel)
    pick_up_current = num_channels_per_pickup * per_tip_pickup_current
    ctx._implementation._hw_manager.hardware._attached_instruments[
        m300._implementation.get_mount()].update_config_item(
        'pick_up_current', pick_up_current)

    tips_ordered = [
        tip for rack in tipracks
        for row in rack.rows()[
                   len(rack.rows()) - num_channels_per_pickup::-1 * num_channels_per_pickup]
        for tip in row]

    tip_count = 0

    def pick_up(pip):
        nonlocal tip_count
        pip.pick_up_tip(tips_ordered[tip_count])
        tip_count += 1

    # Loading in standard labware
    source = ctx.load_labware('eppendorf1.52_24_tuberack_2000ul', 5)

    # Loading in custom labware --> destination plate
    destination = ctx.load_labware('thermo_96_tuberack_500ul', 6)

    #VB.NET
    ##################################################################################################################
    wellplate_source_ab1 = source['A1']
    wellplate_source_ab2 = source['A2']
    wellplate_source_ab3 = source['A3']
    wellplate_source_ab4 = source['A4']
    wellplate_source_ab5 = source['A5']
    wellplate_source_ab6 = source['A6']
    wellplate_source_ab7 = source['D1']
    wellplate_source_ab8 = source['D2']
    wellplate_source_ab9 = source['D3']
    wellplate_source_ab10 = source['D4']
    wellplate_source_ab11 = source['D5']
    wellplate_source_ab12 = source['D6']

    wellplate_destinations_ab1 = [destination['A1'],destination['A2']]
    wellplate_destinations_ab2 = [destination['A3'],destination['A4']]
    wellplate_destinations_ab3 = [destination['A5'],destination['A6']]
    wellplate_destinations_ab4 = [destination['A7'],destination['A8']]
    wellplate_destinations_ab5 = [destination['A9'],destination['A10']]
    wellplate_destinations_ab6 = [destination['A11'],destination['A12']]
    wellplate_destinations_ab7 = [destination['B1'],destination['B2']]
    wellplate_destinations_ab8 = [destination['B3'],destination['B4']]
    wellplate_destinations_ab9 = [destination['B5'],destination['B6']]
    wellplate_destinations_ab10 = [destination['B7'],destination['B8']]
    wellplate_destinations_ab11 = [destination['B9'],destination['B10']]
    wellplate_destinations_ab12 = [destination['B11'],destination['B12']]
	
    ##################################################################################################################
    #Ab1
    pick_up(m300)
    for i in range(len(wellplate_destinations_ab1)):
        m300.aspirate(100, wellplate_source_ab1)
        m300.dispense(100, wellplate_destinations_ab1[i])
    m300.drop_tip()
    #Ab2
    pick_up(m300)
    for i in range(len(wellplate_destinations_ab2)):
        m300.aspirate(100, wellplate_source_ab2)
        m300.dispense(100, wellplate_destinations_ab2[i])
    m300.drop_tip()
    #Ab3
    pick_up(m300)
    for i in range(len(wellplate_destinations_ab3)):
        m300.aspirate(100, wellplate_source_ab3)
        m300.dispense(100, wellplate_destinations_ab3[i])
    m300.drop_tip()
    #Ab4
    pick_up(m300)
    for i in range(len(wellplate_destinations_ab4)):
        m300.aspirate(100, wellplate_source_ab4)
        m300.dispense(100, wellplate_destinations_ab4[i])
    m300.drop_tip()
    #Ab5
    pick_up(m300)
    for i in range(len(wellplate_destinations_ab5)):
        m300.aspirate(100, wellplate_source_ab5)
        m300.dispense(100, wellplate_destinations_ab5[i])
    m300.drop_tip()
    #Ab6
    pick_up(m300)
    for i in range(len(wellplate_destinations_ab6)):
        m300.aspirate(100, wellplate_source_ab6)
        m300.dispense(100, wellplate_destinations_ab6[i])
    m300.drop_tip()
    #Ab7
    pick_up(m300)
    for i in range(len(wellplate_destinations_ab7)):
        m300.aspirate(100, wellplate_source_ab7)
        m300.dispense(100, wellplate_destinations_ab7[i])
    m300.drop_tip()
    #Ab8
    pick_up(m300)
    for i in range(len(wellplate_destinations_ab8)):
        m300.aspirate(100, wellplate_source_ab8)
        m300.dispense(100, wellplate_destinations_ab8[i])
    m300.drop_tip()
    #Ab9
    pick_up(m300)
    for i in range(len(wellplate_destinations_ab9)):
        m300.aspirate(100, wellplate_source_ab9)
        m300.dispense(100, wellplate_destinations_ab9[i])
    m300.drop_tip()
    #Ab10
    pick_up(m300)
    for i in range(len(wellplate_destinations_ab10)):
        m300.aspirate(100, wellplate_source_ab10)
        m300.dispense(100, wellplate_destinations_ab10[i])
    m300.drop_tip()
    #Ab11
    pick_up(m300)
    for i in range(len(wellplate_destinations_ab11)):
        m300.aspirate(100, wellplate_source_ab11)
        m300.dispense(100, wellplate_destinations_ab11[i])
    m300.drop_tip()
    #Ab12
    pick_up(m300)
    for i in range(len(wellplate_destinations_ab12)):
        m300.aspirate(100, wellplate_source_ab12)
        m300.dispense(100, wellplate_destinations_ab12[i])
    m300.drop_tip()
	# lights off
	#ctx.set_rail_lights(on=False)
	#ctx.comment('Protocol complete! Thanks!')
