import json
from opentrons import protocol_api, types


TEST_LABWARE_SLOT = '5'

RATE = 0.25  # % of default speeds

PIPETTE_MOUNT = 'right'
PIPETTE_NAME = 'p300_single_gen2'

TIPRACK_SLOT = '11'
TIPRACK_LOADNAME = 'opentrons_96_tiprack_300ul'
LABWARE_DEF_JSON = """{"ordering":[["A1","B1","C1","D1","E1","F1","G1","H1"],["A2","B2","C2","D2","E2","F2","G2","H2"],["A3","B3","C3","D3","E3","F3","G3","H3"],["A4","B4","C4","D4","E4","F4","G4","H4"],["A5","B5","C5","D5","E5","F5","G5","H5"],["A6","B6","C6","D6","E6","F6","G6","H6"],["A7","B7","C7","D7","E7","F7","G7","H7"],["A8","B8","C8","D8","E8","F8","G8","H8"],["A9","B9","C9","D9","E9","F9","G9","H9"],["A10","B10","C10","D10","E10","F10","G10","H10"],["A11","B11","C11","D11","E11","F11","G11","H11"],["A12","B12","C12","D12","E12","F12","G12","H12"]],"brand":{"brand":"Thermo 96V","brandId":["249944"]},"metadata":{"displayName":"Thermo 96V 96 Well Plate 450 µL","displayCategory":"wellPlate","displayVolumeUnits":"µL","tags":[]},"dimensions":{"xDimension":127,"yDimension":85,"zDimension":14.4},"wells":{"A1":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":14.2,"y":73.7,"z":4.6},"B1":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":14.2,"y":64.8,"z":4.6},"C1":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":14.2,"y":55.9,"z":4.6},"D1":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":14.2,"y":47,"z":4.6},"E1":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":14.2,"y":38.1,"z":4.6},"F1":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":14.2,"y":29.2,"z":4.6},"G1":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":14.2,"y":20.3,"z":4.6},"H1":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":14.2,"y":11.4,"z":4.6},"A2":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":23.1,"y":73.7,"z":4.6},"B2":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":23.1,"y":64.8,"z":4.6},"C2":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":23.1,"y":55.9,"z":4.6},"D2":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":23.1,"y":47,"z":4.6},"E2":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":23.1,"y":38.1,"z":4.6},"F2":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":23.1,"y":29.2,"z":4.6},"G2":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":23.1,"y":20.3,"z":4.6},"H2":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":23.1,"y":11.4,"z":4.6},"A3":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":32,"y":73.7,"z":4.6},"B3":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":32,"y":64.8,"z":4.6},"C3":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":32,"y":55.9,"z":4.6},"D3":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":32,"y":47,"z":4.6},"E3":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":32,"y":38.1,"z":4.6},"F3":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":32,"y":29.2,"z":4.6},"G3":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":32,"y":20.3,"z":4.6},"H3":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":32,"y":11.4,"z":4.6},"A4":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":40.9,"y":73.7,"z":4.6},"B4":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":40.9,"y":64.8,"z":4.6},"C4":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":40.9,"y":55.9,"z":4.6},"D4":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":40.9,"y":47,"z":4.6},"E4":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":40.9,"y":38.1,"z":4.6},"F4":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":40.9,"y":29.2,"z":4.6},"G4":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":40.9,"y":20.3,"z":4.6},"H4":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":40.9,"y":11.4,"z":4.6},"A5":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":49.8,"y":73.7,"z":4.6},"B5":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":49.8,"y":64.8,"z":4.6},"C5":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":49.8,"y":55.9,"z":4.6},"D5":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":49.8,"y":47,"z":4.6},"E5":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":49.8,"y":38.1,"z":4.6},"F5":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":49.8,"y":29.2,"z":4.6},"G5":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":49.8,"y":20.3,"z":4.6},"H5":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":49.8,"y":11.4,"z":4.6},"A6":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":58.7,"y":73.7,"z":4.6},"B6":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":58.7,"y":64.8,"z":4.6},"C6":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":58.7,"y":55.9,"z":4.6},"D6":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":58.7,"y":47,"z":4.6},"E6":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":58.7,"y":38.1,"z":4.6},"F6":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":58.7,"y":29.2,"z":4.6},"G6":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":58.7,"y":20.3,"z":4.6},"H6":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":58.7,"y":11.4,"z":4.6},"A7":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":67.6,"y":73.7,"z":4.6},"B7":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":67.6,"y":64.8,"z":4.6},"C7":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":67.6,"y":55.9,"z":4.6},"D7":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":67.6,"y":47,"z":4.6},"E7":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":67.6,"y":38.1,"z":4.6},"F7":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":67.6,"y":29.2,"z":4.6},"G7":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":67.6,"y":20.3,"z":4.6},"H7":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":67.6,"y":11.4,"z":4.6},"A8":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":76.5,"y":73.7,"z":4.6},"B8":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":76.5,"y":64.8,"z":4.6},"C8":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":76.5,"y":55.9,"z":4.6},"D8":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":76.5,"y":47,"z":4.6},"E8":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":76.5,"y":38.1,"z":4.6},"F8":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":76.5,"y":29.2,"z":4.6},"G8":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":76.5,"y":20.3,"z":4.6},"H8":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":76.5,"y":11.4,"z":4.6},"A9":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":85.4,"y":73.7,"z":4.6},"B9":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":85.4,"y":64.8,"z":4.6},"C9":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":85.4,"y":55.9,"z":4.6},"D9":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":85.4,"y":47,"z":4.6},"E9":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":85.4,"y":38.1,"z":4.6},"F9":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":85.4,"y":29.2,"z":4.6},"G9":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":85.4,"y":20.3,"z":4.6},"H9":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":85.4,"y":11.4,"z":4.6},"A10":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":94.3,"y":73.7,"z":4.6},"B10":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":94.3,"y":64.8,"z":4.6},"C10":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":94.3,"y":55.9,"z":4.6},"D10":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":94.3,"y":47,"z":4.6},"E10":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":94.3,"y":38.1,"z":4.6},"F10":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":94.3,"y":29.2,"z":4.6},"G10":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":94.3,"y":20.3,"z":4.6},"H10":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":94.3,"y":11.4,"z":4.6},"A11":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":103.2,"y":73.7,"z":4.6},"B11":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":103.2,"y":64.8,"z":4.6},"C11":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":103.2,"y":55.9,"z":4.6},"D11":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":103.2,"y":47,"z":4.6},"E11":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":103.2,"y":38.1,"z":4.6},"F11":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":103.2,"y":29.2,"z":4.6},"G11":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":103.2,"y":20.3,"z":4.6},"H11":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":103.2,"y":11.4,"z":4.6},"A12":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":112.1,"y":73.7,"z":4.6},"B12":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":112.1,"y":64.8,"z":4.6},"C12":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":112.1,"y":55.9,"z":4.6},"D12":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":112.1,"y":47,"z":4.6},"E12":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":112.1,"y":38.1,"z":4.6},"F12":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":112.1,"y":29.2,"z":4.6},"G12":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":112.1,"y":20.3,"z":4.6},"H12":{"depth":9.8,"totalLiquidVolume":450,"shape":"circular","diameter":6.7,"x":112.1,"y":11.4,"z":4.6}},"groups":[{"metadata":{"wellBottomShape":"v"},"wells":["A1","B1","C1","D1","E1","F1","G1","H1","A2","B2","C2","D2","E2","F2","G2","H2","A3","B3","C3","D3","E3","F3","G3","H3","A4","B4","C4","D4","E4","F4","G4","H4","A5","B5","C5","D5","E5","F5","G5","H5","A6","B6","C6","D6","E6","F6","G6","H6","A7","B7","C7","D7","E7","F7","G7","H7","A8","B8","C8","D8","E8","F8","G8","H8","A9","B9","C9","D9","E9","F9","G9","H9","A10","B10","C10","D10","E10","F10","G10","H10","A11","B11","C11","D11","E11","F11","G11","H11","A12","B12","C12","D12","E12","F12","G12","H12"]}],"parameters":{"format":"irregular","quirks":[],"isTiprack":false,"isMagneticModuleCompatible":false,"loadName":"thermo96v_96_wellplate_450ul"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}}"""
LABWARE_DEF = json.loads(LABWARE_DEF_JSON)
LABWARE_LABEL = LABWARE_DEF.get('metadata', {}).get(
    'displayName', 'test labware')
LABWARE_DIMENSIONS = LABWARE_DEF.get('wells', {}).get('A1', {}).get('yDimension')

metadata = {'apiLevel': '2.0'}


def run(protocol: protocol_api.ProtocolContext):
    tiprack = protocol.load_labware(TIPRACK_LOADNAME, TIPRACK_SLOT)
    pipette = protocol.load_instrument(
        PIPETTE_NAME, PIPETTE_MOUNT, tip_racks=[tiprack])

    test_labware = protocol.load_labware_from_definition(
        LABWARE_DEF,
        TEST_LABWARE_SLOT,
        LABWARE_LABEL,
    )

    num_cols = len(LABWARE_DEF.get('ordering', [[]]))
    num_rows = len(LABWARE_DEF.get('ordering', [[]])[0])
    total = num_cols * num_rows
    pipette.pick_up_tip()

    def set_speeds(rate):
        protocol.max_speeds.update({
            'X': (600 * rate),
            'Y': (400 * rate),
            'Z': (125 * rate),
            'A': (125 * rate),
        })

        speed_max = max(protocol.max_speeds.values())

        for instr in protocol.loaded_instruments.values():
            instr.default_speed = speed_max

    set_speeds(RATE)

    pipette.home()
    if(PIPETTE_NAME == 'p20_single_gen2' or PIPETTE_NAME == 'p300_single_gen2' or PIPETTE_NAME == 'p1000_single_gen2' or PIPETTE_NAME == 'p50_single' or PIPETTE_NAME == 'p10_single' or PIPETTE_NAME == 'p300_single' or PIPETTE_NAME == 'p1000_single'):
        if(total > 1):
            #testing with single channel
            well = test_labware.well('A1')
            all_4_edges = [
                [well._from_center_cartesian(x=-1, y=0, z=1), 'left'],
                [well._from_center_cartesian(x=1, y=0, z=1), 'right'],
                [well._from_center_cartesian(x=0, y=-1, z=1), 'front'],
                [well._from_center_cartesian(x=0, y=1, z=1), 'back']
            ]

            set_speeds(RATE)
            pipette.move_to(well.top())
            protocol.pause("If the position is accurate click 'resume.'")

            for edge_pos, edge_name in all_4_edges:
                set_speeds(RATE)
                edge_location = types.Location(point=edge_pos, labware=None)
                pipette.move_to(edge_location)
                protocol.pause("If the position is accurate click 'resume.'")
            
            #last well testing
            last_well = (num_cols) * (num_rows)
            well = test_labware.well(last_well-1)
            all_4_edges = [
                [well._from_center_cartesian(x=-1, y=0, z=1), 'left'],
                [well._from_center_cartesian(x=1, y=0, z=1), 'right'],
                [well._from_center_cartesian(x=0, y=-1, z=1), 'front'],
                [well._from_center_cartesian(x=0, y=1, z=1), 'back']
            ]
            for edge_pos, edge_name in all_4_edges:
                set_speeds(RATE)
                edge_location = types.Location(point=edge_pos, labware=None)
                pipette.move_to(edge_location)
                protocol.pause("If the position is accurate click 'resume.'")
            set_speeds(RATE)
            #test bottom of last well
            pipette.move_to(well.bottom())
            protocol.pause("If the position is accurate click 'resume.'")
            pipette.blow_out(well)
        else:
            #testing with single channel + 1 well labware
            well = test_labware.well('A1')
            all_4_edges = [
                [well._from_center_cartesian(x=-1, y=0, z=1), 'left'],
                [well._from_center_cartesian(x=1, y=0, z=1), 'right'],
                [well._from_center_cartesian(x=0, y=-1, z=1), 'front'],
                [well._from_center_cartesian(x=0, y=1, z=1), 'back']
            ]

            set_speeds(RATE)
            pipette.move_to(well.top())
            protocol.pause("If the position is accurate click 'resume.'")

            for edge_pos, edge_name in all_4_edges:
                set_speeds(RATE)
                edge_location = types.Location(point=edge_pos, labware=None)
                pipette.move_to(edge_location)
                protocol.pause("If the position is accurate click 'resume.'")
            
            #test bottom of first well
            well = test_labware.well('A1')
            pipette.move_to(well.bottom())
            protocol.pause("If the position is accurate click 'resume.'")
            pipette.blow_out(well)
    else:
        #testing for multichannel
        if(total == 96 or total == 384): #testing for 96 well plates and 384 first column
            #test first column
            well = test_labware.well('A1')
            all_4_edges = [
                [well._from_center_cartesian(x=-1, y=0, z=1), 'left'],
                [well._from_center_cartesian(x=1, y=0, z=1), 'right'],
                [well._from_center_cartesian(x=0, y=-1, z=1), 'front'],
                [well._from_center_cartesian(x=0, y=1, z=1), 'back']
            ]
            set_speeds(RATE)
            pipette.move_to(well.top())
            protocol.pause("If the position is accurate click 'resume.'")

            for edge_pos, edge_name in all_4_edges:
                set_speeds(RATE)
                edge_location = types.Location(point=edge_pos, labware=None)
                pipette.move_to(edge_location)
                protocol.pause("If the position is accurate click 'resume.'")
            
            #test last column
            if(total == 96):
                last_col = (num_cols * num_rows) - num_rows
                well = test_labware.well(last_col)
                all_4_edges = [
                    [well._from_center_cartesian(x=-1, y=0, z=1), 'left'],
                    [well._from_center_cartesian(x=1, y=0, z=1), 'right'],
                    [well._from_center_cartesian(x=0, y=-1, z=1), 'front'],
                    [well._from_center_cartesian(x=0, y=1, z=1), 'back']
                ]
                for edge_pos, edge_name in all_4_edges:
                    set_speeds(RATE)
                    edge_location = types.Location(point=edge_pos, labware=None)
                    pipette.move_to(edge_location)
                    protocol.pause("If the position is accurate click 'resume.'")
                set_speeds(RATE)
                #test bottom of last column
                pipette.move_to(well.bottom())
                protocol.pause("If the position is accurate click 'resume.'")
                pipette.blow_out(well)
            elif(total == 384):
                #testing for 384 well plates - need to hit well 369, last column
                well369 = (total) - (num_rows) + 1
                well = test_labware.well(well369)
                pipette.move_to(well.top())
                protocol.pause("If the position is accurate click 'resume.'")
                all_4_edges = [
                    [well._from_center_cartesian(x=-1, y=0, z=1), 'left'],
                    [well._from_center_cartesian(x=1, y=0, z=1), 'right'],
                    [well._from_center_cartesian(x=0, y=-1, z=1), 'front'],
                    [well._from_center_cartesian(x=0, y=1, z=1), 'back']
                ]
                for edge_pos, edge_name in all_4_edges:
                    set_speeds(RATE)
                    edge_location = types.Location(point=edge_pos, labware=None)
                    pipette.move_to(edge_location)
                    protocol.pause("If the position is accurate click 'resume.'")
                set_speeds(RATE)
                #test bottom of last column
                pipette.move_to(well.bottom())
                protocol.pause("If the position is accurate click 'resume.'")
                pipette.blow_out(well)
        elif(num_rows == 1 and total > 1 and LABWARE_DIMENSIONS >= 71.2):
            #for 1 row reservoirs - ex: 12 well reservoirs
            well = test_labware.well('A1')
            all_4_edges = [
                [well._from_center_cartesian(x=-1, y=1, z=1), 'left'],
                [well._from_center_cartesian(x=1, y=1, z=1), 'right'],
                [well._from_center_cartesian(x=0, y=0.75, z=1), 'front'],
                [well._from_center_cartesian(x=0, y=1, z=1), 'back']
            ]
            set_speeds(RATE)
            pipette.move_to(well.top())
            protocol.pause("If the position is accurate click 'resume.'")

            for edge_pos, edge_name in all_4_edges:
                set_speeds(RATE)
                edge_location = types.Location(point=edge_pos, labware=None)
                pipette.move_to(edge_location)
                protocol.pause("If the position is accurate click 'resume.'")
            #test last well
            well = test_labware.well(-1)
            all_4_edges = [
                [well._from_center_cartesian(x=-1, y=1, z=1), 'left'],
                [well._from_center_cartesian(x=1, y=1, z=1), 'right'],
                [well._from_center_cartesian(x=0, y=0.75, z=1), 'front'],
                [well._from_center_cartesian(x=0, y=1, z=1), 'back']
            ]
            set_speeds(RATE)

            for edge_pos, edge_name in all_4_edges:
                set_speeds(RATE)
                edge_location = types.Location(point=edge_pos, labware=None)
                pipette.move_to(edge_location)
                protocol.pause("If the position is accurate click 'resume.'")
                #test bottom of first well
            pipette.move_to(well.bottom())
            protocol.pause("If the position is accurate click 'resume.'")
            pipette.blow_out(well)

        
        elif(total == 1 and LABWARE_DIMENSIONS >= 71.2 ):
            #for 1 well reservoirs
            well = test_labware.well('A1')
            all_4_edges = [
                [well._from_center_cartesian(x=-1, y=1, z=1), 'left'],
                [well._from_center_cartesian(x=1, y=1, z=1), 'right'],
                [well._from_center_cartesian(x=0, y=0.75, z=1), 'front'],
                [well._from_center_cartesian(x=0, y=1, z=1), 'back']
            ]
            set_speeds(RATE)
            pipette.move_to(well.top())
            protocol.pause("If the position is accurate click 'resume.'")

            for edge_pos, edge_name in all_4_edges:
                set_speeds(RATE)
                edge_location = types.Location(point=edge_pos, labware=None)
                pipette.move_to(edge_location)
                protocol.pause("If the position is accurate click 'resume.'")
                #test bottom of first well
            pipette.move_to(well.bottom())
            protocol.pause("If the position is accurate click 'resume.'")
            pipette.blow_out(well)
        
        else:
            #for incompatible labwares
            protocol.pause("labware is incompatible to calibrate with a multichannel pipette")




    set_speeds(1.0)
    pipette.return_tip()