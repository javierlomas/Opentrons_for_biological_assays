from opentrons import protocol_api

metadata = {
    'protocolName': 'Serial Dilution 384 jlomas',
    'apiLevel': '2.11',
    'author': 'Javier Lomas'}

def run(ctx):
    '''
        @javierlomas
        Full plate, serial dilution from columns 3-12;13-22, 5ul transfer to 20ul (1/5) in base 3 mixes of 15ul, changing tips
        test 202203041156: 11:29 min
        test 202203041215: 12:25 min
        test 202203041235: 15:08 min
        test 202203041300: 23:20 min (392 steps)
    '''
    # turn on the lights, let's the party begin
    ctx.set_rail_lights(on=True)

    # Loading tipracks, pipette instrument and working plate
    tiprack = [ctx.load_labware('opentrons_96_tiprack_20ul', '4'),ctx.load_labware('opentrons_96_tiprack_20ul', '1'),ctx.load_labware('opentrons_96_tiprack_20ul', '7'),ctx.load_labware('opentrons_96_tiprack_20ul', '10')]
    m20 = ctx.load_instrument('p20_multi_gen2', 'left',tiprack)
    plate = ctx.load_labware('nunc384shallowellpp264573_384_wellplate_115ul', 5)

    #Assay variables
    transfer_volume=5
    number_of_mixes=3
    volume_for_mix=15

    #Half plate dropping tips every time
    columns = [3, 4, 5 , 6 , 7, 8, 9, 10, 11]
    #First mix
    m20.pick_up_tip()
    m20.mix(number_of_mixes, volume_for_mix, plate['A3'])
    m20.drop_tip()
    # Serially dilute up (works fine)
    for i in columns[:9]:
        m20.pick_up_tip()
        m20.transfer(transfer_volume, plate[f"A{i}"], plate[f"A{i + 1}"], mix_after=(number_of_mixes, volume_for_mix), new_tip="never")
        m20.drop_tip()

    # Serially dilute down (works fine)
    m20.pick_up_tip()
    m20.mix(number_of_mixes, volume_for_mix, plate['B3'])
    m20.drop_tip()
    for i in columns[:9]:
        m20.pick_up_tip()
        m20.transfer(transfer_volume, plate[f"B{i}"], plate[f"B{i + 1}"], mix_after=(number_of_mixes, volume_for_mix), new_tip="never")
        m20.drop_tip()

    #The other half plate (works fine)
    columns = [13, 14, 15, 16, 17, 18, 19, 20, 21]
    m20.pick_up_tip()
    m20.mix(number_of_mixes, volume_for_mix, plate['A13'])
    m20.drop_tip()
    for i in columns[:9]:
        m20.pick_up_tip()
        m20.transfer(transfer_volume, plate[f"A{i}"], plate[f"A{i + 1}"], mix_after=(number_of_mixes, volume_for_mix), new_tip="never")
        m20.drop_tip()

    # Serially dilute down (works fine)
    m20.pick_up_tip()
    m20.mix(number_of_mixes, volume_for_mix, plate['B13'])
    m20.drop_tip()
    for i in columns[:9]:
        m20.pick_up_tip()
        m20.transfer(transfer_volume, plate[f"B{i}"], plate[f"B{i + 1}"], mix_after=(number_of_mixes, volume_for_mix), new_tip="never")
        m20.drop_tip()
    # lights off, let's go to sleep
    ctx.set_rail_lights(on=False)