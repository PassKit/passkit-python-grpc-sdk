# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: io/flights/a_rpc.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from io.flights import boarding_pass_pb2 as io_dot_flights_dot_boarding__pass__pb2
from io.flights import airport_pb2 as io_dot_flights_dot_airport__pb2
from io.flights import flight_pb2 as io_dot_flights_dot_flight__pb2
from io.flights import flight_designator_pb2 as io_dot_flights_dot_flight__designator__pb2
from io.flights import carrier_pb2 as io_dot_flights_dot_carrier__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16io/flights/a_rpc.proto\x12\x07\x66lights\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a\x1eio/flights/boarding_pass.proto\x1a\x18io/flights/airport.proto\x1a\x17io/flights/flight.proto\x1a\"io/flights/flight_designator.proto\x1a\x18io/flights/carrier.proto2\x97\x38\n\x07\x46lights\x12\xf2\x01\n\ncreatePort\x12\r.flights.Port\x1a\x16.google.protobuf.Empty\"\xbc\x01\x82\xd3\xe4\x93\x02\x15\"\x10/flights/airport:\x01*\x92\x41\x9d\x01\n\x08\x41irports\x12\x0e\x43reate Airport\x1a\x19\x43reates an airport recordJ0\n\x03\x34\x30\x30\x12)\n\'There is a problem with the input data.J4\n\x03\x34\x30\x33\x12-\n+Returned when the user lacks authorization.\x12\xd2\x01\n\x07getPort\x12\x14.flights.AirportCode\x1a\r.flights.Port\"\xa1\x01\x82\xd3\xe4\x93\x02 \x12\x1e/flights/airport/{airportCode}\x92\x41x\n\x08\x41irports\x12\x0bGet Airport\x1a\x1bRetrieves an airport recordJ\"\n\x03\x34\x30\x33\x12\x1b\n\x19User lacks authorization.J\x1e\n\x03\x34\x30\x34\x12\x17\n\x15Record was not found.\x12\xd0\x02\n\nupdatePort\x12\r.flights.Port\x1a\r.flights.Port\"\xa3\x02\x82\xd3\xe4\x93\x02\x15\x1a\x10/flights/airport:\x01*\x92\x41\x84\x02\n\x08\x41irports\x12\x0eUpdate Airport\x1a\x19Updates an airport recordJ0\n\x03\x34\x30\x30\x12)\n\'There is a problem with the input data.J\"\n\x03\x34\x30\x33\x12\x1b\n\x19User lacks authorization.J\x1e\n\x03\x34\x30\x34\x12\x17\n\x15Record was not found.JW\n\x03\x35\x30\x33\x12P\nNServer is unavailable. Back off for 250ms and repeat request until successful.\x12\xe7\x01\n\ndeletePort\x12\x14.flights.AirportCode\x1a\x16.google.protobuf.Empty\"\xaa\x01\x82\xd3\xe4\x93\x02\x15*\x10/flights/airport:\x01*\x92\x41\x8b\x01\n\x08\x41irports\x12\x0e\x44\x65lete Airport\x1a\x19\x44\x65letes a airport record.J4\n\x03\x34\x30\x33\x12-\n+Returned when the user lacks authorization.J\x1e\n\x03\x34\x30\x34\x12\x17\n\x15Record was not found.\x12\xf7\x01\n\rcreateCarrier\x12\x10.flights.Carrier\x1a\x16.google.protobuf.Empty\"\xbb\x01\x82\xd3\xe4\x93\x02\x15\"\x10/flights/carrier:\x01*\x92\x41\x9c\x01\n\x08\x43\x61rriers\x12\x0e\x43reate Carrier\x1a\x18\x43reates a carrier recordJ0\n\x03\x34\x30\x30\x12)\n\'There is a problem with the input data.J4\n\x03\x34\x30\x33\x12-\n+Returned when the user lacks authorization.\x12\xd7\x01\n\ngetCarrier\x12\x14.flights.CarrierCode\x1a\x10.flights.Carrier\"\xa0\x01\x82\xd3\xe4\x93\x02 \x12\x1e/flights/carrier/{carrierCode}\x92\x41w\n\x08\x43\x61rriers\x12\x0bGet Carrier\x1a\x1aRetrieves a carrier recordJ\"\n\x03\x34\x30\x33\x12\x1b\n\x19User lacks authorization.J\x1e\n\x03\x34\x30\x34\x12\x17\n\x15Record was not found.\x12\xd8\x02\n\rupdateCarrier\x12\x10.flights.Carrier\x1a\x10.flights.Carrier\"\xa2\x02\x82\xd3\xe4\x93\x02\x15\x1a\x10/flights/carrier:\x01*\x92\x41\x83\x02\n\x08\x43\x61rriers\x12\x0eUpdate Carrier\x1a\x18Updates a carrier recordJ0\n\x03\x34\x30\x30\x12)\n\'There is a problem with the input data.J\"\n\x03\x34\x30\x33\x12\x1b\n\x19User lacks authorization.J\x1e\n\x03\x34\x30\x34\x12\x17\n\x15Record was not found.JW\n\x03\x35\x30\x33\x12P\nNServer is unavailable. Back off for 250ms and repeat request until successful.\x12\xea\x01\n\rdeleteCarrier\x12\x14.flights.CarrierCode\x1a\x16.google.protobuf.Empty\"\xaa\x01\x82\xd3\xe4\x93\x02\x15*\x10/flights/carrier:\x01*\x92\x41\x8b\x01\n\x08\x43\x61rriers\x12\x0e\x44\x65lete Carrier\x1a\x19\x44\x65letes a carrier record.J4\n\x03\x34\x30\x33\x12-\n+Returned when the user lacks authorization.J\x1e\n\x03\x34\x30\x34\x12\x17\n\x15Record was not found.\x12\x92\x03\n\x16\x63reateFlightDesignator\x12\x19.flights.FlightDesignator\x1a\x16.google.protobuf.Empty\"\xc4\x02\x82\xd3\xe4\x93\x02\x18\"\x13/flights/designator:\x01*\x92\x41\xa2\x02\n\x12\x46light Designators\x12\x19\x43reate Flight Designation\x1a\"Creates a flight designator recordJ0\n\x03\x34\x30\x30\x12)\n\'There is a problem with the input data.J\"\n\x03\x34\x30\x33\x12\x1b\n\x19User lacks authorization.J\x1e\n\x03\x34\x30\x34\x12\x17\n\x15Record was not found.JW\n\x03\x35\x30\x33\x12P\nNServer is unavailable. Back off for 250ms and repeat request until successful.\x12\xb2\x02\n\x13getFlightDesignator\x12 .flights.FlightDesignatorRequest\x1a\x19.flights.FlightDesignator\"\xdd\x01\x82\xd3\xe4\x93\x02=\x12;/flights/designator/{carrierCode}/{flightNumber}/{revision}\x92\x41\x96\x01\n\x12\x46light Designators\x12\x16Get Flight Designation\x1a$Retrieves a flight designator recordJ\"\n\x03\x34\x30\x33\x12\x1b\n\x19User lacks authorization.J\x1e\n\x03\x34\x30\x34\x12\x17\n\x15Record was not found.\x12\x95\x03\n\x16updateFlightDesignator\x12\x19.flights.FlightDesignator\x1a\x19.flights.FlightDesignator\"\xc4\x02\x82\xd3\xe4\x93\x02\x18\x1a\x13/flights/designator:\x01*\x92\x41\xa2\x02\n\x12\x46light Designators\x12\x19Update Flight Designation\x1a\"Updates a flight designator recordJ0\n\x03\x34\x30\x30\x12)\n\'There is a problem with the input data.J\"\n\x03\x34\x30\x33\x12\x1b\n\x19User lacks authorization.J\x1e\n\x03\x34\x30\x34\x12\x17\n\x15Record was not found.JW\n\x03\x35\x30\x33\x12P\nNServer is unavailable. Back off for 250ms and repeat request until successful.\x12\x8f\x02\n\x16\x64\x65leteFlightDesignator\x12 .flights.FlightDesignatorRequest\x1a\x16.google.protobuf.Empty\"\xba\x01\x82\xd3\xe4\x93\x02\x18*\x13/flights/designator:\x01*\x92\x41\x98\x01\n\x12\x46light Designators\x12\x19\x44\x65lete Flight Designation\x1a#Deletes a flight designator record.J\"\n\x03\x34\x30\x33\x12\x1b\n\x19User lacks authorization.J\x1e\n\x03\x34\x30\x34\x12\x17\n\x15Record was not found.\x12\xc0\x03\n\x0c\x63reateFlight\x12\x0f.flights.Flight\x1a\x16.google.protobuf.Empty\"\x86\x03\x82\xd3\xe4\x93\x02\x14\"\x0f/flights/flight:\x01*\x92\x41\xe8\x02\n\x07\x46lights\x12\rCreate Flight\x1a~Creates a flight record.  Note that this method will often not be used, since new flight records can be automatically created.J0\n\x03\x34\x30\x30\x12)\n\'There is a problem with the input data.J\"\n\x03\x34\x30\x33\x12\x1b\n\x19User lacks authorization.J\x1f\n\x03\x34\x30\x39\x12\x18\n\x16Record already exists.JW\n\x03\x35\x30\x33\x12P\nNServer is unavailable. Back off for 250ms and repeat request until successful.\x12\xc4\x02\n\tgetFlight\x12\x16.flights.FlightRequest\x1a\x0f.flights.Flight\"\x8d\x02\x82\xd3\xe4\x93\x02\x8f\x01\x12\x8c\x01/flights/flight/{carrierCode}/{flightNumber}/{departureDate.year}/{departureDate.month}/{departureDate.day}/{boardingPoint}/{deplaningPoint}\x92\x41t\n\x07\x46lights\x12\nGet Flight\x1a\x19Retrieves a flight recordJ\"\n\x03\x34\x30\x33\x12\x1b\n\x19User lacks authorization.J\x1e\n\x03\x34\x30\x34\x12\x17\n\x15Record was not found.\x12\x89\x04\n\x0cupdateFlight\x12\x0f.flights.Flight\x1a\x0f.flights.Flight\"\xd6\x03\x82\xd3\xe4\x93\x02\x14\x1a\x0f/flights/flight:\x01*\x92\x41\xb8\x03\n\x07\x46lights\x12\x14Update Flight Number\x1a\xc7\x01Updates a flight number record.  Note that if the flight number is subscribed to automatic flight alerts, this method may not be required and that changes made may be overwritten by automatic updatesJ0\n\x03\x34\x30\x30\x12)\n\'There is a problem with the input data.J\"\n\x03\x34\x30\x33\x12\x1b\n\x19User lacks authorization.J\x1e\n\x03\x34\x30\x34\x12\x17\n\x15Record was not found.JW\n\x03\x35\x30\x33\x12P\nNServer is unavailable. Back off for 250ms and repeat request until successful.\x12\xdd\x02\n\x0c\x64\x65leteFlight\x12\x16.flights.FlightRequest\x1a\x16.google.protobuf.Empty\"\x9c\x02\x82\xd3\xe4\x93\x02\x14*\x0f/flights/flight:\x01*\x92\x41\xfe\x01\n\x07\x46lights\x12\rDelete Flight\x1a\x9f\x01\x44\x65letes a flight record. Note that a deleted flight record may be automatically recreated, unless the [active] flag on the Flight Number record is set to falseJ\"\n\x03\x34\x30\x33\x12\x1b\n\x19User lacks authorization.J\x1e\n\x03\x34\x30\x34\x12\x17\n\x15Record was not found.\x12\x91\x04\n\x12\x63reateBoardingPass\x12\x1b.flights.BoardingPassRecord\x1a\x1f.flights.BoardingPassesResponse\"\xbc\x03\x82\xd3\xe4\x93\x02\x1a\"\x15/flights/boardingPass:\x01*\x92\x41\x98\x03\n\x0f\x42oarding Passes\x12\x14\x43reate Boarding Pass\x1a\x9e\x01\x43reates a boarding pass record. If flight record for the date does not yet exist, it will be created using the Flight Designation defaults. Returns a pass id.J0\n\x03\x34\x30\x30\x12)\n\'There is a problem with the input data.J\"\n\x03\x34\x30\x33\x12\x1b\n\x19User lacks authorization.J\x1f\n\x03\x34\x30\x39\x12\x18\n\x16Record already exists.JW\n\x03\x35\x30\x33\x12P\nNServer is unavailable. Back off for 250ms and repeat request until successful.\x12\xca\x02\n\x15getBoardingPassRecord\x12\".flights.BoardingPassRecordRequest\x1a\x1b.flights.BoardingPassRecord\"\xef\x01\x82\xd3\xe4\x93\x02\x1c\"\x17/flights/boardingRecord:\x01*\x92\x41\xc9\x01\n\x0f\x42oarding Passes\x12\x18Get Boarding Pass Record\x1aXRetrieves a boarding pass record. One of ticketNumber, index or passId must be provided.J\"\n\x03\x34\x30\x33\x12\x1b\n\x19User lacks authorization.J\x1e\n\x03\x34\x30\x34\x12\x17\n\x15Record was not found.\x12\xe9\x02\n\x0fgetBoardingPass\x12\x1c.flights.BoardingPassRequest\x1a\x1f.flights.BoardingPassesResponse\"\x96\x02\x82\xd3\xe4\x93\x02\x12\"\r/flights/pass:\x01*\x92\x41\xfa\x01\n\x0f\x42oarding Passes\x12\x11Get Boarding Pass\x1a\x8f\x01Retrieves digital boarding pass(es) in the requested format based on the index provided. Supply only one of ticketNumber, index, pnr or passId.J\"\n\x03\x34\x30\x33\x12\x1b\n\x19User lacks authorization.J\x1e\n\x03\x34\x30\x34\x12\x17\n\x15Record was not found.\x12\xaa\x04\n\x12updateBoardingPass\x12\x1b.flights.BoardingPassRecord\x1a\x1b.flights.BoardingPassRecord\"\xd9\x03\x82\xd3\xe4\x93\x02\x1c\x1a\x17/flights/boardingRecord:\x01*\x92\x41\xb3\x03\n\x0f\x42oarding Passes\x12\x14Update Boarding Pass\x1a\xba\x01Updates a boarding pass record. Either ticketNumber and ticketLeg or carrier, flight number, flightDate, boardingPoint and sequenceNumber must be provided. All other fields are optional.J0\n\x03\x34\x30\x30\x12)\n\'There is a problem with the input data.J\"\n\x03\x34\x30\x33\x12\x1b\n\x19User lacks authorization.J\x1e\n\x03\x34\x30\x34\x12\x17\n\x15Record was not found.JW\n\x03\x35\x30\x33\x12P\nNServer is unavailable. Back off for 250ms and repeat request until successful.\x12\x84\x02\n\x12\x64\x65leteBoardingPass\x12\".flights.BoardingPassRecordRequest\x1a\x16.google.protobuf.Empty\"\xb1\x01\x82\xd3\xe4\x93\x02\x1c*\x17/flights/boardingRecord:\x01*\x92\x41\x8b\x01\n\x0f\x42oarding Passes\x12\x14\x44\x65lete Boarding Pass\x1a\x1e\x44\x65letes a boarding pass recordJ\"\n\x03\x34\x30\x33\x12\x1b\n\x19User lacks authorization.J\x1e\n\x03\x34\x30\x34\x12\x17\n\x15Record was not found.B\x8d\x03\n\x18\x63om.passkit.grpc.FlightsZ,stash.passkit.com/io/model/sdk/go/io/flights\xaa\x02\x14PassKit.Grpc.Flights\x92\x41\xaa\x02\x12\x80\x02\n\x13PassKit Flights API\x12iThe PassKit Flights API lets you manage your flights and boarding passes for Apple Wallet and Google Pay.\x1a\x38https://passkit.com/legal/terms-of-subscription-service/\"?\n\x0fPassKit Support\x12\x17https://docs.passkit.io\x1a\x13support@passkit.com2\x03\x30.1*\x01\x02\x32\x10\x61pplication/json:\x10\x61pplication/jsonb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'io.flights.a_rpc_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.passkit.grpc.FlightsZ,stash.passkit.com/io/model/sdk/go/io/flights\252\002\024PassKit.Grpc.Flights\222A\252\002\022\200\002\n\023PassKit Flights API\022iThe PassKit Flights API lets you manage your flights and boarding passes for Apple Wallet and Google Pay.\0328https://passkit.com/legal/terms-of-subscription-service/\"?\n\017PassKit Support\022\027https://docs.passkit.io\032\023support@passkit.com2\0030.1*\001\0022\020application/json:\020application/json'
  _FLIGHTS.methods_by_name['createPort']._options = None
  _FLIGHTS.methods_by_name['createPort']._serialized_options = b'\202\323\344\223\002\025\"\020/flights/airport:\001*\222A\235\001\n\010Airports\022\016Create Airport\032\031Creates an airport recordJ0\n\003400\022)\n\'There is a problem with the input data.J4\n\003403\022-\n+Returned when the user lacks authorization.'
  _FLIGHTS.methods_by_name['getPort']._options = None
  _FLIGHTS.methods_by_name['getPort']._serialized_options = b'\202\323\344\223\002 \022\036/flights/airport/{airportCode}\222Ax\n\010Airports\022\013Get Airport\032\033Retrieves an airport recordJ\"\n\003403\022\033\n\031User lacks authorization.J\036\n\003404\022\027\n\025Record was not found.'
  _FLIGHTS.methods_by_name['updatePort']._options = None
  _FLIGHTS.methods_by_name['updatePort']._serialized_options = b'\202\323\344\223\002\025\032\020/flights/airport:\001*\222A\204\002\n\010Airports\022\016Update Airport\032\031Updates an airport recordJ0\n\003400\022)\n\'There is a problem with the input data.J\"\n\003403\022\033\n\031User lacks authorization.J\036\n\003404\022\027\n\025Record was not found.JW\n\003503\022P\nNServer is unavailable. Back off for 250ms and repeat request until successful.'
  _FLIGHTS.methods_by_name['deletePort']._options = None
  _FLIGHTS.methods_by_name['deletePort']._serialized_options = b'\202\323\344\223\002\025*\020/flights/airport:\001*\222A\213\001\n\010Airports\022\016Delete Airport\032\031Deletes a airport record.J4\n\003403\022-\n+Returned when the user lacks authorization.J\036\n\003404\022\027\n\025Record was not found.'
  _FLIGHTS.methods_by_name['createCarrier']._options = None
  _FLIGHTS.methods_by_name['createCarrier']._serialized_options = b'\202\323\344\223\002\025\"\020/flights/carrier:\001*\222A\234\001\n\010Carriers\022\016Create Carrier\032\030Creates a carrier recordJ0\n\003400\022)\n\'There is a problem with the input data.J4\n\003403\022-\n+Returned when the user lacks authorization.'
  _FLIGHTS.methods_by_name['getCarrier']._options = None
  _FLIGHTS.methods_by_name['getCarrier']._serialized_options = b'\202\323\344\223\002 \022\036/flights/carrier/{carrierCode}\222Aw\n\010Carriers\022\013Get Carrier\032\032Retrieves a carrier recordJ\"\n\003403\022\033\n\031User lacks authorization.J\036\n\003404\022\027\n\025Record was not found.'
  _FLIGHTS.methods_by_name['updateCarrier']._options = None
  _FLIGHTS.methods_by_name['updateCarrier']._serialized_options = b'\202\323\344\223\002\025\032\020/flights/carrier:\001*\222A\203\002\n\010Carriers\022\016Update Carrier\032\030Updates a carrier recordJ0\n\003400\022)\n\'There is a problem with the input data.J\"\n\003403\022\033\n\031User lacks authorization.J\036\n\003404\022\027\n\025Record was not found.JW\n\003503\022P\nNServer is unavailable. Back off for 250ms and repeat request until successful.'
  _FLIGHTS.methods_by_name['deleteCarrier']._options = None
  _FLIGHTS.methods_by_name['deleteCarrier']._serialized_options = b'\202\323\344\223\002\025*\020/flights/carrier:\001*\222A\213\001\n\010Carriers\022\016Delete Carrier\032\031Deletes a carrier record.J4\n\003403\022-\n+Returned when the user lacks authorization.J\036\n\003404\022\027\n\025Record was not found.'
  _FLIGHTS.methods_by_name['createFlightDesignator']._options = None
  _FLIGHTS.methods_by_name['createFlightDesignator']._serialized_options = b'\202\323\344\223\002\030\"\023/flights/designator:\001*\222A\242\002\n\022Flight Designators\022\031Create Flight Designation\032\"Creates a flight designator recordJ0\n\003400\022)\n\'There is a problem with the input data.J\"\n\003403\022\033\n\031User lacks authorization.J\036\n\003404\022\027\n\025Record was not found.JW\n\003503\022P\nNServer is unavailable. Back off for 250ms and repeat request until successful.'
  _FLIGHTS.methods_by_name['getFlightDesignator']._options = None
  _FLIGHTS.methods_by_name['getFlightDesignator']._serialized_options = b'\202\323\344\223\002=\022;/flights/designator/{carrierCode}/{flightNumber}/{revision}\222A\226\001\n\022Flight Designators\022\026Get Flight Designation\032$Retrieves a flight designator recordJ\"\n\003403\022\033\n\031User lacks authorization.J\036\n\003404\022\027\n\025Record was not found.'
  _FLIGHTS.methods_by_name['updateFlightDesignator']._options = None
  _FLIGHTS.methods_by_name['updateFlightDesignator']._serialized_options = b'\202\323\344\223\002\030\032\023/flights/designator:\001*\222A\242\002\n\022Flight Designators\022\031Update Flight Designation\032\"Updates a flight designator recordJ0\n\003400\022)\n\'There is a problem with the input data.J\"\n\003403\022\033\n\031User lacks authorization.J\036\n\003404\022\027\n\025Record was not found.JW\n\003503\022P\nNServer is unavailable. Back off for 250ms and repeat request until successful.'
  _FLIGHTS.methods_by_name['deleteFlightDesignator']._options = None
  _FLIGHTS.methods_by_name['deleteFlightDesignator']._serialized_options = b'\202\323\344\223\002\030*\023/flights/designator:\001*\222A\230\001\n\022Flight Designators\022\031Delete Flight Designation\032#Deletes a flight designator record.J\"\n\003403\022\033\n\031User lacks authorization.J\036\n\003404\022\027\n\025Record was not found.'
  _FLIGHTS.methods_by_name['createFlight']._options = None
  _FLIGHTS.methods_by_name['createFlight']._serialized_options = b'\202\323\344\223\002\024\"\017/flights/flight:\001*\222A\350\002\n\007Flights\022\rCreate Flight\032~Creates a flight record.  Note that this method will often not be used, since new flight records can be automatically created.J0\n\003400\022)\n\'There is a problem with the input data.J\"\n\003403\022\033\n\031User lacks authorization.J\037\n\003409\022\030\n\026Record already exists.JW\n\003503\022P\nNServer is unavailable. Back off for 250ms and repeat request until successful.'
  _FLIGHTS.methods_by_name['getFlight']._options = None
  _FLIGHTS.methods_by_name['getFlight']._serialized_options = b'\202\323\344\223\002\217\001\022\214\001/flights/flight/{carrierCode}/{flightNumber}/{departureDate.year}/{departureDate.month}/{departureDate.day}/{boardingPoint}/{deplaningPoint}\222At\n\007Flights\022\nGet Flight\032\031Retrieves a flight recordJ\"\n\003403\022\033\n\031User lacks authorization.J\036\n\003404\022\027\n\025Record was not found.'
  _FLIGHTS.methods_by_name['updateFlight']._options = None
  _FLIGHTS.methods_by_name['updateFlight']._serialized_options = b'\202\323\344\223\002\024\032\017/flights/flight:\001*\222A\270\003\n\007Flights\022\024Update Flight Number\032\307\001Updates a flight number record.  Note that if the flight number is subscribed to automatic flight alerts, this method may not be required and that changes made may be overwritten by automatic updatesJ0\n\003400\022)\n\'There is a problem with the input data.J\"\n\003403\022\033\n\031User lacks authorization.J\036\n\003404\022\027\n\025Record was not found.JW\n\003503\022P\nNServer is unavailable. Back off for 250ms and repeat request until successful.'
  _FLIGHTS.methods_by_name['deleteFlight']._options = None
  _FLIGHTS.methods_by_name['deleteFlight']._serialized_options = b'\202\323\344\223\002\024*\017/flights/flight:\001*\222A\376\001\n\007Flights\022\rDelete Flight\032\237\001Deletes a flight record. Note that a deleted flight record may be automatically recreated, unless the [active] flag on the Flight Number record is set to falseJ\"\n\003403\022\033\n\031User lacks authorization.J\036\n\003404\022\027\n\025Record was not found.'
  _FLIGHTS.methods_by_name['createBoardingPass']._options = None
  _FLIGHTS.methods_by_name['createBoardingPass']._serialized_options = b'\202\323\344\223\002\032\"\025/flights/boardingPass:\001*\222A\230\003\n\017Boarding Passes\022\024Create Boarding Pass\032\236\001Creates a boarding pass record. If flight record for the date does not yet exist, it will be created using the Flight Designation defaults. Returns a pass id.J0\n\003400\022)\n\'There is a problem with the input data.J\"\n\003403\022\033\n\031User lacks authorization.J\037\n\003409\022\030\n\026Record already exists.JW\n\003503\022P\nNServer is unavailable. Back off for 250ms and repeat request until successful.'
  _FLIGHTS.methods_by_name['getBoardingPassRecord']._options = None
  _FLIGHTS.methods_by_name['getBoardingPassRecord']._serialized_options = b'\202\323\344\223\002\034\"\027/flights/boardingRecord:\001*\222A\311\001\n\017Boarding Passes\022\030Get Boarding Pass Record\032XRetrieves a boarding pass record. One of ticketNumber, index or passId must be provided.J\"\n\003403\022\033\n\031User lacks authorization.J\036\n\003404\022\027\n\025Record was not found.'
  _FLIGHTS.methods_by_name['getBoardingPass']._options = None
  _FLIGHTS.methods_by_name['getBoardingPass']._serialized_options = b'\202\323\344\223\002\022\"\r/flights/pass:\001*\222A\372\001\n\017Boarding Passes\022\021Get Boarding Pass\032\217\001Retrieves digital boarding pass(es) in the requested format based on the index provided. Supply only one of ticketNumber, index, pnr or passId.J\"\n\003403\022\033\n\031User lacks authorization.J\036\n\003404\022\027\n\025Record was not found.'
  _FLIGHTS.methods_by_name['updateBoardingPass']._options = None
  _FLIGHTS.methods_by_name['updateBoardingPass']._serialized_options = b'\202\323\344\223\002\034\032\027/flights/boardingRecord:\001*\222A\263\003\n\017Boarding Passes\022\024Update Boarding Pass\032\272\001Updates a boarding pass record. Either ticketNumber and ticketLeg or carrier, flight number, flightDate, boardingPoint and sequenceNumber must be provided. All other fields are optional.J0\n\003400\022)\n\'There is a problem with the input data.J\"\n\003403\022\033\n\031User lacks authorization.J\036\n\003404\022\027\n\025Record was not found.JW\n\003503\022P\nNServer is unavailable. Back off for 250ms and repeat request until successful.'
  _FLIGHTS.methods_by_name['deleteBoardingPass']._options = None
  _FLIGHTS.methods_by_name['deleteBoardingPass']._serialized_options = b'\202\323\344\223\002\034*\027/flights/boardingRecord:\001*\222A\213\001\n\017Boarding Passes\022\024Delete Boarding Pass\032\036Deletes a boarding pass recordJ\"\n\003403\022\033\n\031User lacks authorization.J\036\n\003404\022\027\n\025Record was not found.'
  _FLIGHTS._serialized_start=288
  _FLIGHTS._serialized_end=7479
# @@protoc_insertion_point(module_scope)