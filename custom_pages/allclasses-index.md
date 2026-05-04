---
title: "All Classes and Interfaces (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestallclasses-index"
hidden: false
---

# All Classes and Interfaces

All Classes and Interfaces

Interfaces

Classes

Enum Classes

Exceptions
Class
Description
[AccessAttributes](sdk-for-android-explore-api-reference-latestaccessattributes "enum class in com.here.sdk.routing")
Types of access attributes.
[Address](sdk-for-android-explore-api-reference-latestaddress "class in com.here.sdk.search")
Information about the address of a location.
[AddressQuery](sdk-for-android-explore-api-reference-latestaddressquery "class in com.here.sdk.search")
The options to specify an address query.
[AddressType](sdk-for-android-explore-api-reference-latestaddresstype "enum class in com.here.sdk.search")
Address type
[Agency](sdk-for-android-explore-api-reference-latestagency "class in com.here.sdk.routing")
Holds all the agency information.
[AllowOptions](sdk-for-android-explore-api-reference-latestallowoptions "class in com.here.sdk.routing")
The options explicitly allowed by user for route calculations.
[Anchor2D](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core")
Represents a point in a rectangle as a ratio of this rectangle's width and height.
[Anchor2DKeyframe](sdk-for-android-explore-api-reference-latestanchor2dkeyframe "class in com.here.sdk.animation")
An Anchor2D keyframe.
[Angle](sdk-for-android-explore-api-reference-latestangle "class in com.here.sdk.core")
Represents an angle independent of the unit of measurement.
[AngleRange](sdk-for-android-explore-api-reference-latestanglerange "class in com.here.sdk.core")
Represents angle ranges as a circular sector by using an absolute start angle and a relative range angle called extent.
[AnimationListener](sdk-for-android-explore-api-reference-latestanimationlistener "interface in com.here.sdk.animation")
A listener for animation events.
[AnimationState](sdk-for-android-explore-api-reference-latestanimationstate "enum class in com.here.sdk.animation")
Describes the possible states of an animation.
[ApplicationUtilsInitializer](sdk-for-android-explore-api-reference-latestapplicationutilsinitializer "class in com.here.sdk.core.engine")
This class is for internal use only.
[AreaType](sdk-for-android-explore-api-reference-latestareatype "enum class in com.here.sdk.search")
Represents a type of area like country, state, city, county, etc.
[AssetsManager](sdk-for-android-explore-api-reference-latestassetsmanager "class in com.here.sdk.mapview")
Assets manager interface.
[Attribution](sdk-for-android-explore-api-reference-latestattribution "class in com.here.sdk.routing")
Holds all the data on a URL address to an external resource.
[AttributionType](sdk-for-android-explore-api-reference-latestattributiontype "enum class in com.here.sdk.routing")
Attribution link type.
[Authentication](sdk-for-android-explore-api-reference-latestauthentication "class in com.here.sdk.core")
Use the authentication class to authenticate and retrieve a secure token that can be used with other HERE services.
[AuthenticationCallback](sdk-for-android-explore-api-reference-latestauthenticationcallback "interface in com.here.sdk.core")
Callback passed to [`Authentication.authenticate(SDKNativeEngine)`](sdk-for-android-explore-api-reference-latestauthentication#authenticate(com.here.sdk.core.engine.SDKNativeEngine)).
[AuthenticationData](sdk-for-android-explore-api-reference-latestauthenticationdata "class in com.here.sdk.core")
Authentication data
[AuthenticationError](sdk-for-android-explore-api-reference-latestauthenticationerror "enum class in com.here.sdk.core")
Authentication error
[AuthenticationException](sdk-for-android-explore-api-reference-latestauthenticationexception "class in com.here.sdk.core")
Authentication exception
[AuthenticationMode](sdk-for-android-explore-api-reference-latestauthenticationmode "class in com.here.sdk.core.engine")
This is a bearer authentication mode which adds or does not add a header ("Authorization", "Bearer \$Token") to each online request of the module the object is added to.
[AuthenticationMode.AccessTokenProvider](sdk-for-android-explore-api-reference-latestauthenticationmode-accesstokenprovider "interface in com.here.sdk.core.engine")
This lambda is used to retrieve access token in synchronous manner.
[AvoidanceOptions](sdk-for-android-explore-api-reference-latestavoidanceoptions "class in com.here.sdk.routing")
The options to specify restrictions for route calculations.
[AvoidBoundingBoxAreaOptions](sdk-for-android-explore-api-reference-latestavoidboundingboxareaoptions "class in com.here.sdk.routing")
The options to specify rectangular shape which routes must not cross.
[AvoidCorridorAreaOptions](sdk-for-android-explore-api-reference-latestavoidcorridorareaoptions "class in com.here.sdk.routing")
Area of corridor shape which routes must not cross and exceptions for this area.
[AvoidPolygonAreaOptions](sdk-for-android-explore-api-reference-latestavoidpolygonareaoptions "class in com.here.sdk.routing")
The options to specify polygon shape which routes must not cross.
[BatterySpecifications](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing")
Parameters related to the electric vehicle's battery.
[BicycleOptions](sdk-for-android-explore-api-reference-latestbicycleoptions "class in com.here.sdk.routing")
Deprecated.
Will be removed in v4.28.0.
[BusinessDetails](sdk-for-android-explore-api-reference-latestbusinessdetails "class in com.here.sdk.search")
Contains place details such as contacts, opening hours and some electro vehicle info.
[BusOptions](sdk-for-android-explore-api-reference-latestbusoptions "class in com.here.sdk.routing")
Deprecated.
Will be removed in v4.28.0.
[BusSpecifications](sdk-for-android-explore-api-reference-latestbusspecifications "class in com.here.sdk.transport")
Bus specifications contain vehicle related attributes.
[CalculateIsolineCallback](sdk-for-android-explore-api-reference-latestcalculateisolinecallback "interface in com.here.sdk.routing")
A function which is called by the RoutingEngine after isoline calculation has completed.
[CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")
A function which is called by the RoutingEngine after route calculation has completed.
[CalculateTrafficOnRouteCallback](sdk-for-android-explore-api-reference-latestcalculatetrafficonroutecallback "interface in com.here.sdk.routing")
A function which is called by the RoutingEngine after route traffic calculation has completed.
[CardinalDirection](sdk-for-android-explore-api-reference-latestcardinaldirection "enum class in com.here.sdk.core")
Indicates the official directional identifier assigned to this road.
[CarOptions](sdk-for-android-explore-api-reference-latestcaroptions "class in com.here.sdk.routing")
Deprecated.
Will be removed in v4.28.0.
[CarSpecifications](sdk-for-android-explore-api-reference-latestcarspecifications "class in com.here.sdk.transport")
Car specifications contain vehicle related attributes.
[CatalogConfiguration](sdk-for-android-explore-api-reference-latestcatalogconfiguration "class in com.here.sdk.core.engine")
Using this class you can configure in the [`SDKOptions`](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine"), how the [`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") should access, use and store the data for the desired catalog.
[CatalogIdentifier](sdk-for-android-explore-api-reference-latestcatalogidentifier "class in com.here.sdk.core.engine")
This class is used to identify any catalog in the HERE platform.
[CatalogType](sdk-for-android-explore-api-reference-latestcatalogtype "enum class in com.here.sdk.core.engine")
Represents default HERE catalog types.
[CatalogVersionHint](sdk-for-android-explore-api-reference-latestcatalogversionhint "class in com.here.sdk.core.engine")
This is a class for capturing user's intent for the desired catalog version to use in [`DesiredCatalog`](sdk-for-android-explore-api-reference-latestdesiredcatalog "class in com.here.sdk.core.engine") class.
[CategoryQuery](sdk-for-android-explore-api-reference-latestcategoryquery "class in com.here.sdk.search")
The options to specify a query by categories.
[CategoryQuery.Area](sdk-for-android-explore-api-reference-latestcategoryquery-area "class in com.here.sdk.search")
Area to perform search on.
[CertificateSettings](sdk-for-android-explore-api-reference-latestcertificatesettings "class in com.here.sdk.core.engine")
Certificate settings to be used by Curl+OpenSSL for authority
[ChargingActionDetails](sdk-for-android-explore-api-reference-latestchargingactiondetails "class in com.here.sdk.routing")
Parameters related to the electric vehicle's charging action.
[ChargingConnectorAttributes](sdk-for-android-explore-api-reference-latestchargingconnectorattributes "class in com.here.sdk.routing")
Details of the connector that is suggested to be used in the section's [`PostAction`](sdk-for-android-explore-api-reference-latestpostaction "class in com.here.sdk.routing")'s for charging.
[ChargingConnectorType](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")
Available charging connector types.
[ChargingStation](sdk-for-android-explore-api-reference-latestchargingstation "class in com.here.sdk.routing")
Data for an electric vehicle charging station.
[ChargingStop](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing")
The options to specify a user-planned charging stop.
[ChargingSupplyType](sdk-for-android-explore-api-reference-latestchargingsupplytype "enum class in com.here.sdk.routing")
Available charging supply types.
[Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")
Represents a color value.
[Contact](sdk-for-android-explore-api-reference-latestcontact "class in com.here.sdk.search")
Represents contact information.
[CountryCode](sdk-for-android-explore-api-reference-latestcountrycode "enum class in com.here.sdk.core")
This enum represents country codes in accordance with the ISO 3166-1 standard using alpha-3 codes.
[CurrentType](sdk-for-android-explore-api-reference-latestcurrenttype "enum class in com.here.sdk.core")
This enum represents the type of electric current
[CustomMetadataValue](sdk-for-android-explore-api-reference-latestcustommetadatavalue "interface in com.here.sdk.core")
Interface for storing arbitrary metadata types.
[DashPattern](sdk-for-android-explore-api-reference-latestdashpattern "class in com.here.sdk.mapview")
Represents a dash pattern for map polyline.
[DataAttributes](sdk-for-android-explore-api-reference-latestdataattributes "class in com.here.sdk.mapview.datasource")
Data attributes collection.
[DataAttributesAccessor](sdk-for-android-explore-api-reference-latestdataattributesaccessor "class in com.here.sdk.mapview.datasource")
Accessor used for manipulating data attributes.
[DataAttributesBase](sdk-for-android-explore-api-reference-latestdataattributesbase "interface in com.here.sdk.mapview.datasource")
Interface for a collection of data attributes.
[DataAttributesBuilder](sdk-for-android-explore-api-reference-latestdataattributesbuilder "class in com.here.sdk.mapview.datasource")
Data attributes collection builder.
[DataAttributeValue](sdk-for-android-explore-api-reference-latestdataattributevalue "class in com.here.sdk.mapview.datasource")
Encapsulates a data attribute value.
[DataAttributeValue.ValueType](sdk-for-android-explore-api-reference-latestdataattributevalue-valuetype "enum class in com.here.sdk.mapview.datasource")
Supported types of the data attribute values.
[DesiredCatalog](sdk-for-android-explore-api-reference-latestdesiredcatalog "class in com.here.sdk.core.engine")
This class provides an interface to the user, to identify a catalog on the HERE platform, whose data he wants to access.
[Details](sdk-for-android-explore-api-reference-latestdetails "class in com.here.sdk.search")
Contains details of a specific place, such as contact information, opening hours and assigned categories.
[DeviceIdCallback](sdk-for-android-explore-api-reference-latestdeviceidcallback "interface in com.here.sdk.core.engine")
This method will be called on the main thread when [`SDKNativeEngine.getDeviceId(com.here.sdk.core.engine.DeviceIdCallback)`](sdk-for-android-explore-api-reference-latestsdknativeengine#getDeviceId(com.here.sdk.core.engine.DeviceIdCallback)) has been completed.
[DoubleTapListener](sdk-for-android-explore-api-reference-latestdoubletaplistener "interface in com.here.sdk.gestures")
Interface for handling double tap gestures.
[DrawOrderType](sdk-for-android-explore-api-reference-latestdrawordertype "enum class in com.here.sdk.mapview")
Specifies the type of map item draw order.
[Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")
Represents duration in time (both positive and negative).
[DynamicSpeedInfo](sdk-for-android-explore-api-reference-latestdynamicspeedinfo "class in com.here.sdk.routing")
Provides estimated speed information.
[Easing](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation")
Animation easing representing an easing function to be used during animations.
[Easing.InstantiationErrorCode](sdk-for-android-explore-api-reference-latesteasing-instantiationerrorcode "enum class in com.here.sdk.animation")
Describes a reason for failing to create an [`Easing`](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation").
[Easing.InstantiationException](sdk-for-android-explore-api-reference-latesteasing-instantiationexception "class in com.here.sdk.animation")
Thrown when a problem occurs while trying to create an [`Easing`](sdk-for-android-explore-api-reference-latesteasing "class in com.here.sdk.animation").
[EasingFunction](sdk-for-android-explore-api-reference-latesteasingfunction "enum class in com.here.sdk.animation")
Animation easing functions.
[ElectricVehicleOptions](sdk-for-android-explore-api-reference-latestelectricvehicleoptions "class in com.here.sdk.routing")
These options define the parameters of the electric vehicle.
[EmailAddress](sdk-for-android-explore-api-reference-latestemailaddress "class in com.here.sdk.search")
Represents data related to specific email address.
[EMobilityServiceProvider](sdk-for-android-explore-api-reference-latestemobilityserviceprovider "class in com.here.sdk.search")
eMSP (e-Mobility Service Provider) for which the EV station operator has EV roaming agreements.
[EmpiricalConsumptionModel](sdk-for-android-explore-api-reference-latestempiricalconsumptionmodel "class in com.here.sdk.routing")
This model defines a data-driven energy consumption model for electric vehicles.
[EngineBaseURL](sdk-for-android-explore-api-reference-latestenginebaseurl "enum class in com.here.sdk.core.engine")
Lists the available HERE SDK endpoints that can be customized with a custom backend base URL.
[EngineOptions](sdk-for-android-explore-api-reference-latestengineoptions "class in com.here.sdk.core.engine")
Specifies several options specific to different engines.
[EVAccessRestrictionReason](sdk-for-android-explore-api-reference-latestevaccessrestrictionreason "enum class in com.here.sdk.search")
Represents the restriction reason of an `EVChargingPool`.
[EVAccessType](sdk-for-android-explore-api-reference-latestevaccesstype "enum class in com.here.sdk.search")
Represents the accessibility level of an `EVChargingPool`.
[EVCarOptions](sdk-for-android-explore-api-reference-latestevcaroptions "class in com.here.sdk.routing")
Deprecated.
Will be removed in v4.28.0.
[EVChargingPool](sdk-for-android-explore-api-reference-latestevchargingpool "class in com.here.sdk.search")
A charging pool for electric vehicles is an area equipped with one or more charging stations.
[EVChargingPoolDetails](sdk-for-android-explore-api-reference-latestevchargingpooldetails "class in com.here.sdk.search")
Electric vehicle charging pool details.
[EVChargingStation](sdk-for-android-explore-api-reference-latestevchargingstation "class in com.here.sdk.search")
Group of connectors for electric vehicles (EVs), defined by a common charging connector type and maximum power level.
[EVConsumptionModel](sdk-for-android-explore-api-reference-latestevconsumptionmodel "class in com.here.sdk.routing")
Parameters specific for the electric vehicle, which are then used to calculate energy consumption on a given route.
[EVMobilityServiceProviderPreferences](sdk-for-android-explore-api-reference-latestevmobilityserviceproviderpreferences "class in com.here.sdk.routing")
Defines preference level per known E-Mobility Service Provider.
[Evse](sdk-for-android-explore-api-reference-latestevse "class in com.here.sdk.search")
Charge Point Operator (CPO) ID uses the Electric Vehicle Supply Equipment ID (EVSE ID) for an exact identification of the charging infrastructure and charging point.
[EVSEConnector](sdk-for-android-explore-api-reference-latestevseconnector "class in com.here.sdk.search")
EVSE connector.
[EVSEStatus](sdk-for-android-explore-api-reference-latestevsestatus "enum class in com.here.sdk.search")
EVSE status
[EVTruckOptions](sdk-for-android-explore-api-reference-latestevtruckoptions "class in com.here.sdk.routing")
Deprecated.
Will be removed in v4.28.0.
[ExternalID](sdk-for-android-explore-api-reference-latestexternalid "class in com.here.sdk.core")
Identifier of the entity as provided by the external source
[Fare](sdk-for-android-explore-api-reference-latestfare "class in com.here.sdk.routing")
Holds all the fare data.
[FarePassValidityPeriod](sdk-for-android-explore-api-reference-latestfarepassvalidityperiod "class in com.here.sdk.routing")
Specifies a temporal validity period for a pass
[FarePassValidityPeriodType](sdk-for-android-explore-api-reference-latestfarepassvalidityperiodtype "enum class in com.here.sdk.routing")
Specifies validity periods.
[FarePrice](sdk-for-android-explore-api-reference-latestfareprice "class in com.here.sdk.routing")
Price of a fare.
[FarePriceType](sdk-for-android-explore-api-reference-latestfarepricetype "enum class in com.here.sdk.routing")
Type of price represented by a [`FarePrice`](sdk-for-android-explore-api-reference-latestfareprice "class in com.here.sdk.routing") object.
[FareReason](sdk-for-android-explore-api-reference-latestfarereason "enum class in com.here.sdk.routing")
Reason for the cost.
[FlingHandler](sdk-for-android-explore-api-reference-latestflinghandler "class in com.here.sdk.gestures")
This class handles fling events by performing a kinetic move on the map.
[FuelAdditive](sdk-for-android-explore-api-reference-latestfueladditive "class in com.here.sdk.search")
Contains fuel additive information for generic fuel type.
[FuelAdditiveType](sdk-for-android-explore-api-reference-latestfueladditivetype "enum class in com.here.sdk.transport")
Defines possible fuel additives that a fuel could contain.
[FuelStation](sdk-for-android-explore-api-reference-latestfuelstation "class in com.here.sdk.search")
Contains information about a specific fuel station.
[FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport")
Defines possible fuel types provided by a fuel station.
[FunctionalRoadClass](sdk-for-android-explore-api-reference-latestfunctionalroadclass "enum class in com.here.sdk.routing")
Types of function road class.
[GeneralVehicleSpeedLimits](sdk-for-android-explore-api-reference-latestgeneralvehiclespeedlimits "class in com.here.sdk.transport")
Contains the speed limits for vehicles in a country / state.
[GenericFuel](sdk-for-android-explore-api-reference-latestgenericfuel "class in com.here.sdk.search")
Contains generic fuel type info of fuel station.
[GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")
Represents a bounding rectangle aligned with latitude and longitude.
[GeoCircle](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core")
Represents a circle area in 2D space.
[GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")
Represents geographical coordinates in 3D space.
[GeoCoordinatesKeyframe](sdk-for-android-explore-api-reference-latestgeocoordinateskeyframe "class in com.here.sdk.animation")
A GeoCoordinatesKeyframe consists of a GeoCoordinates and an animation duration.
[GeoCoordinatesUpdate](sdk-for-android-explore-api-reference-latestgeocoordinatesupdate "class in com.here.sdk.core")
Represents geographical coordinates in 3D space.
[GeoCorridor](sdk-for-android-explore-api-reference-latestgeocorridor "class in com.here.sdk.core")
A geographical area that wraps around a geographical polyline with a given distance.
[GeoOrientation](sdk-for-android-explore-api-reference-latestgeoorientation "class in com.here.sdk.core")
Geodetic orientation with bearing, tilt and roll.
[GeoOrientationKeyframe](sdk-for-android-explore-api-reference-latestgeoorientationkeyframe "class in com.here.sdk.animation")
A GeoOrientationKeyframe consists of a GeoOrientation (camera orientation) and an animation duration.
[GeoOrientationUpdate](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core")
Describes geodetic orientation update with bearing and tilt.
[GeoPlace](sdk-for-android-explore-api-reference-latestgeoplace "class in com.here.sdk.search")
GeoPlace struct represents a location object: such as a country, a city, a point of interest (POI) etc.
[GeoPolygon](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core")
Represents a `GeoPolygon` area as a series of geographic coordinates, and optionally, a list of inner boundaries (also known as holes).
[GeoPolyline](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core")
A list of geographic coordinates representing the vertices of a polyline.
[GeoPolylineDirection](sdk-for-android-explore-api-reference-latestgeopolylinedirection "enum class in com.here.sdk.core")
Defines if a function on a [`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core") computes the operation starting from the beginning or from the end of [`GeoPolyline.vertices`](sdk-for-android-explore-api-reference-latestgeopolyline#vertices).
[Gestures](sdk-for-android-explore-api-reference-latestgestures "class in com.here.sdk.gestures")
Use this class to process touch events from the platform and detect gesture induced actions on the map view.
[GestureState](sdk-for-android-explore-api-reference-latestgesturestate "enum class in com.here.sdk.gestures")
Represents the state of the gesture.
[GestureType](sdk-for-android-explore-api-reference-latestgesturetype "enum class in com.here.sdk.gestures")
Enum that represents the type of a gesture.
[HazardousMaterial](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport")
Identifiers for different types of hazardous materials which can be shipped by the truck.
[HereMap](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview")
The representation of a dynamic and interactive geographic map.
[HighlightType](sdk-for-android-explore-api-reference-latesthighlighttype "enum class in com.here.sdk.search")
Specifies members of Suggestion class to which input query can be matched.
[IconProvider](sdk-for-android-explore-api-reference-latesticonprovider "class in com.here.sdk.mapview")
This provider creates icons from a given set of parameters for map content and constraints for icon dimensions for a particular map scheme.
[IconProvider.IconCallback](sdk-for-android-explore-api-reference-latesticonprovider-iconcallback "interface in com.here.sdk.mapview")
Interface which is used as callback to pass back an image or error code after calling the createRoadShieldIcon() method.
[IconProviderAssetType](sdk-for-android-explore-api-reference-latesticonproviderassettype "enum class in com.here.sdk.mapview")
Asset types for loading icons.
[IconProviderError](sdk-for-android-explore-api-reference-latesticonprovidererror "enum class in com.here.sdk.mapview")
Error which indicates why an icon could not be retrieved.
[ImageFormat](sdk-for-android-explore-api-reference-latestimageformat "enum class in com.here.sdk.mapview")
Image format.
[IndexRange](android-sdk-apirange "class in com.here.sdk.search")
Holds information to which part of the text, input query was matched.
[InitProvider](sdk-for-android-explore-api-reference-latestinitprovider "class in com.here.sdk.engine")
Performs global initialization of the SDK.
[InstantiationErrorCode](sdk-for-android-explore-api-reference-latestinstantiationerrorcode "enum class in com.here.sdk.core.errors")
Instantiation error.
[InstantiationErrorException](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors")
Instantiation error.
[IntegerRange](sdk-for-android-explore-api-reference-latestintegerrange "class in com.here.sdk.core")
An integer range \[min, max\] with inclusive minimum and maximum value.
[Isoline](sdk-for-android-explore-api-reference-latestisoline "class in com.here.sdk.routing")
Represents an isoline polygon around a center point.
[IsolineCalculationMode](sdk-for-android-explore-api-reference-latestisolinecalculationmode "enum class in com.here.sdk.routing")
Specifies how isoline calculation is optimized.
[IsolineOptions](sdk-for-android-explore-api-reference-latestisolineoptions "class in com.here.sdk.routing")
Specifies options for isolines calculation.
[IsolineOptions.Calculation](sdk-for-android-explore-api-reference-latestisolineoptions-calculation "class in com.here.sdk.routing")
Specifies isoline parameters.
[IsolineRangeType](sdk-for-android-explore-api-reference-latestisolinerangetype "enum class in com.here.sdk.routing")
Specifies the type of one or more range values to be included in the isoline.
[IsolineRoutingEngine](sdk-for-android-explore-api-reference-latestisolineroutingengine "class in com.here.sdk.routing")
Use the IsolineRoutingEngine to calculate a reachable area from a center point.
[JsonStyleFactory](sdk-for-android-explore-api-reference-latestjsonstylefactory "class in com.here.sdk.mapview")
A factory of [`Style`](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview") objects from styles defined in JSON format.
[JsonStyleFactory.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestjsonstylefactory-instantiationerrorcode "enum class in com.here.sdk.mapview")
Describes reasons for failing to create a [`Style`](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview") from a JSON source.
[JsonStyleFactory.InstantiationErrorDetails](sdk-for-android-explore-api-reference-latestjsonstylefactory-instantiationerrordetails "class in com.here.sdk.mapview")
Describes the reason for failing to create a [`Style`](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview") from a JSON source.
[JsonStyleFactory.InstantiationException](sdk-for-android-explore-api-reference-latestjsonstylefactory-instantiationexception "class in com.here.sdk.mapview")
Thrown when failing to create a [`Style`](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview") from a JSON source.
[JunctionsTraversability](sdk-for-android-explore-api-reference-latestjunctionstraversability "enum class in com.here.sdk.traffic")
Junctions traversability of some traffic incident or flow section.
[KeyframeInterpolationMode](sdk-for-android-explore-api-reference-latestkeyframeinterpolationmode "enum class in com.here.sdk.animation")
Specifies type of interpolation performed between keyframes.
[LandlinePhone](sdk-for-android-explore-api-reference-latestlandlinephone "class in com.here.sdk.search")
Represents data related to specific landline phone number.
[LanguageCode](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core")
This enum represents language codes.
[LayerConfiguration](sdk-for-android-explore-api-reference-latestlayerconfiguration "class in com.here.sdk.core.engine")
A class to configure which layers should be enabled or disabled in the OCM map data.
[LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine")
Defines a list of possible map data features that can be enabled / disabled.
[LineCap](sdk-for-android-explore-api-reference-latestlinecap "enum class in com.here.sdk.mapview")
Determines the cap (line ending) style.
[LineData](sdk-for-android-explore-api-reference-latestlinedata "class in com.here.sdk.mapview.datasource")
Represents a geodetic line with custom attributes.
[LineDataAccessor](sdk-for-android-explore-api-reference-latestlinedataaccessor "class in com.here.sdk.mapview.datasource")
Line data accessor used for manipulating polylines that are part of a LineDataSource.
[LineDataBuilder](sdk-for-android-explore-api-reference-latestlinedatabuilder "class in com.here.sdk.mapview.datasource")
Builder of [`LineData`](sdk-for-android-explore-api-reference-latestlinedata "class in com.here.sdk.mapview.datasource") instances.
[LineDataSource](sdk-for-android-explore-api-reference-latestlinedatasource "class in com.here.sdk.mapview.datasource")
Polyline data source allows the rendering engine access to the user provided polylines geometry and their attributes.
[LineDataSource.LineDataProcessor](sdk-for-android-explore-api-reference-latestlinedatasource-linedataprocessor "interface in com.here.sdk.mapview.datasource")
Called for each line, allowing inspection, removal or update of coordinates and attributes.
[LineDataSourceBuilder](sdk-for-android-explore-api-reference-latestlinedatasourcebuilder "class in com.here.sdk.mapview.datasource")
Builder of lines data source.
[LineTileDataSource](sdk-for-android-explore-api-reference-latestlinetiledatasource "class in com.here.sdk.mapview.datasource")
Line tile data source allows the rendering engine access to user managed data sets of geodetic lines and their attributes through a [`LineTileSource`](sdk-for-android-explore-api-reference-latestlinetilesource "interface in com.here.sdk.mapview.datasource").
[LineTileSource](sdk-for-android-explore-api-reference-latestlinetilesource "interface in com.here.sdk.mapview.datasource")
A source of geodetic line tiles.
[LineTileSource.LoadResultHandler](sdk-for-android-explore-api-reference-latestlinetilesource-loadresulthandler "interface in com.here.sdk.mapview.datasource")
Result handler of a load tile request.
[LocalizedRoadNumber](sdk-for-android-explore-api-reference-latestlocalizedroadnumber "class in com.here.sdk.routing")
Used to represent road number localized to specific language with optional direction and route type information.
[LocalizedRoadNumbers](sdk-for-android-explore-api-reference-latestlocalizedroadnumbers "class in com.here.sdk.routing")
The list of multiple names or titles for the same entity, possibly in different languages.
[LocalizedText](sdk-for-android-explore-api-reference-latestlocalizedtext "class in com.here.sdk.core")
Used to represent text localized to specific language.
[LocalizedTextPreference](sdk-for-android-explore-api-reference-latestlocalizedtextpreference "enum class in com.here.sdk.routing")
Indicates the option of localized text usage.
[LocalizedTexts](sdk-for-android-explore-api-reference-latestlocalizedtexts "class in com.here.sdk.core")
The list of multiple names or titles for the same entity, possibly in different languages.
[Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")
Describes a location in the world at a given time.
[LocationDetails](sdk-for-android-explore-api-reference-latestlocationdetails "class in com.here.sdk.search")
Contains geographical info about location
[LocationIndicator](sdk-for-android-explore-api-reference-latestlocationindicator "class in com.here.sdk.mapview")
Graphical object to represent the location of the user on the map.
[LocationIndicator.IndicatorStyle](sdk-for-android-explore-api-reference-latestlocationindicator-indicatorstyle "enum class in com.here.sdk.mapview")
The predefined styles for the location indicator which are pedestrian and navigation mode.
[LocationIndicator.MarkerType](sdk-for-android-explore-api-reference-latestlocationindicator-markertype "enum class in com.here.sdk.mapview")
Enum to identify different types of markers of the location indicator.
[LocationListener](sdk-for-android-explore-api-reference-latestlocationlistener "interface in com.here.sdk.core")
This interface should be implemented in order to receive notifications about location updates.
[LocationSource](sdk-for-android-explore-api-reference-latestlocationsource "enum class in com.here.sdk.core")
Indicates where the location was computed.
[LocationTechnology](sdk-for-android-explore-api-reference-latestlocationtechnology "enum class in com.here.sdk.core")
Technology or provider of the location.
[LocationTime](sdk-for-android-explore-api-reference-latestlocationtime "class in com.here.sdk.core")
This struct presents all the time data tied to a location, like an arrival or departure time.
[LockingProcess](sdk-for-android-explore-api-reference-latestlockingprocess "class in com.here.sdk.core.engine")
LockingProcess helps to detect situations when cache is locked with another process and attempt to create instance of [`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") fails with error [`InstantiationErrorCode.FAILED_TO_LOCK_CACHE_FOLDER`](sdk-for-android-explore-api-reference-latestinstantiationerrorcode#FAILED_TO_LOCK_CACHE_FOLDER).
[LogAppender](sdk-for-android-explore-api-reference-latestlogappender "interface in com.here.sdk.core.engine")
An interface to implement a listener to receive log messages.
[LogControl](sdk-for-android-explore-api-reference-latestlogcontrol "class in com.here.sdk.core.engine")
This class provides functionality to enable/disable console logs as well as setting a custom log appender to receive log messages from the SDK.
[LogControl.InvalidPathException](sdk-for-android-explore-api-reference-latestlogcontrol-invalidpathexception "class in com.here.sdk.core.engine")
Invalid file path exception.
[LogLevel](sdk-for-android-explore-api-reference-latestloglevel "enum class in com.here.sdk.core.engine")
Severity levels for log messages.
[LongPressListener](sdk-for-android-explore-api-reference-latestlongpresslistener "interface in com.here.sdk.gestures")
Interface for handling long-press gestures.
[Maneuver](sdk-for-android-explore-api-reference-latestmaneuver "class in com.here.sdk.routing")
This class provides all the information for a maneuver.
[ManeuverAction](sdk-for-android-explore-api-reference-latestmaneuveraction "enum class in com.here.sdk.routing")
Maneuver action type.
[MapArrow](sdk-for-android-explore-api-reference-latestmaparrow "class in com.here.sdk.mapview")
A visual representation of an arrow on the map.
[MapCamera](sdk-for-android-explore-api-reference-latestmapcamera "class in com.here.sdk.mapview")
Represents the camera looking onto the map view.
[MapCamera.DryCameraUpdateCallback](sdk-for-android-explore-api-reference-latestmapcamera-drycameraupdatecallback "interface in com.here.sdk.mapview")
Used to report back results of dry update application to camera.
[MapCamera.FarPlaneConfiguration](sdk-for-android-explore-api-reference-latestmapcamera-farplaneconfiguration "class in com.here.sdk.mapview")
Far plane distance configuration for a zoom level.
[MapCamera.State](sdk-for-android-explore-api-reference-latestmapcamera-state "class in com.here.sdk.mapview")
Encapsulates state of the camera.
[MapCameraAnimation](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview")
An animation that can be applied to a [`MapCamera`](sdk-for-android-explore-api-reference-latestmapcamera "class in com.here.sdk.mapview").
[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")
Describes a reason for failing to create a multi-track [`MapCameraAnimation`](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview").
[MapCameraAnimation.InstantiationException](sdk-for-android-explore-api-reference-latestmapcameraanimation-instantiationexception "class in com.here.sdk.mapview")
Thrown when a problem occurs while trying to create a multi-track [`MapCameraAnimation`](sdk-for-android-explore-api-reference-latestmapcameraanimation "class in com.here.sdk.mapview").
[MapCameraAnimationFactory](sdk-for-android-explore-api-reference-latestmapcameraanimationfactory "class in com.here.sdk.mapview")
Factory for creating MapCameraAnimation objects to change map's camera over time.
[MapCameraKeyframeTrack](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack "class in com.here.sdk.mapview")
Stores keyframes for interpolation of a camera property using a specific easing function and interpolation mode.
[MapCameraKeyframeTrack.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack-instantiationerrorcode "enum class in com.here.sdk.mapview")
Describes a reason for failing to create a MapCameraKeyframeTrack.
[MapCameraKeyframeTrack.InstantiationException](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack-instantiationexception "class in com.here.sdk.mapview")
Thrown when a problem occurs while trying to create [`MapCameraKeyframeTrack`](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack "class in com.here.sdk.mapview").
[MapCameraLimits](sdk-for-android-explore-api-reference-latestmapcameralimits "class in com.here.sdk.mapview")
Controls constraints on map camera parameters.
[MapCameraListener](sdk-for-android-explore-api-reference-latestmapcameralistener "interface in com.here.sdk.mapview")
Interface for objects that want to get updates whenever the map is redrawn after camera parameters change.
[MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")
An update that can be applied to the map camera.
[MapCameraUpdate.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapcameraupdate-instantiationerrorcode "enum class in com.here.sdk.mapview")
Describes a reason for failing to create a [`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview").
[MapCameraUpdate.InstantiationException](sdk-for-android-explore-api-reference-latestmapcameraupdate-instantiationexception "class in com.here.sdk.mapview")
Thrown when a problem occurs while trying to create a [`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview").
[MapCameraUpdateFactory](sdk-for-android-explore-api-reference-latestmapcameraupdatefactory "class in com.here.sdk.mapview")
Factory for creating MapCameraUpdate to change map's camera.
[MapContentCategory](sdk-for-android-explore-api-reference-latestmapcontentcategory "enum class in com.here.sdk.mapview")
Type representing map content categories.
[MapContentSettings](sdk-for-android-explore-api-reference-latestmapcontentsettings "class in com.here.sdk.mapview")
Provides settings regarding map data which are applied globally to all map views.
[MapContentSettings.TrafficRefreshPeriodErrorCode](sdk-for-android-explore-api-reference-latestmapcontentsettings-trafficrefreshperioderrorcode "enum class in com.here.sdk.mapview")
Traffic refresh period error code
[MapContentSettings.TrafficRefreshPeriodException](sdk-for-android-explore-api-reference-latestmapcontentsettings-trafficrefreshperiodexception "class in com.here.sdk.mapview")
Traffic refresh period error exception
[MapContentType](sdk-for-android-explore-api-reference-latestmapcontenttype "enum class in com.here.sdk.mapview")
Content types supported by the map.
[MapContext](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview")
MapContext is the rendering engine and the context in which virtual geographic maps get rendered.
[MapContext.FreeResourceSeverity](sdk-for-android-explore-api-reference-latestmapcontext-freeresourceseverity "enum class in com.here.sdk.mapview")
The severity of a free resource request.
[MapContext.MemoryManagementOptions](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementoptions "class in com.here.sdk.mapview")
Memory management options.
[MapContext.MemoryManagementResult](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresult "class in com.here.sdk.mapview")
Memory management result.
[MapContext.MemoryManagementResultCode](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementresultcode "enum class in com.here.sdk.mapview")
The memory management result code.
[MapContext.MemoryManagementStrategy](sdk-for-android-explore-api-reference-latestmapcontext-memorymanagementstrategy "enum class in com.here.sdk.mapview")
The memory management strategy.
[MapContext.ResourceType](sdk-for-android-explore-api-reference-latestmapcontext-resourcetype "enum class in com.here.sdk.mapview")
Types of system resources used by [`MapContext`](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview") or any of the entities attached to it, like [`HereMap`](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview").
[MapContext.SetMemoryManagementOptionsCallback](sdk-for-android-explore-api-reference-latestmapcontext-setmemorymanagementoptionscallback "interface in com.here.sdk.mapview")
Callback to handle the memory management result.
[MapError](sdk-for-android-explore-api-reference-latestmaperror "enum class in com.here.sdk.mapview")
Represents various errors that could occur from map related operations.
[MapFeatureModes](sdk-for-android-explore-api-reference-latestmapfeaturemodes "class in com.here.sdk.mapview")
Holds constants for map feature modes, to be used with [`MapScene.enableFeatures(java.util.Map<java.lang.String, java.lang.String>)`](sdk-for-android-explore-api-reference-latestmapscene#enableFeatures(java.util.Map)).
[MapFeatures](sdk-for-android-explore-api-reference-latestmapfeatures "class in com.here.sdk.mapview")
Holds constants for map features, to be used with [`MapScene.enableFeatures(java.util.Map<java.lang.String, java.lang.String>)`](sdk-for-android-explore-api-reference-latestmapscene#enableFeatures(java.util.Map)) and [`MapScene.disableFeatures(java.util.List<java.lang.String>)`](sdk-for-android-explore-api-reference-latestmapscene#disableFeatures(java.util.List)).
[MapIdleListener](sdk-for-android-explore-api-reference-latestmapidlelistener "interface in com.here.sdk.mapview")
Used to detect when the map becomes idle or busy.
[MapImage](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview")
Represents a drawable resource that can be used by a [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview"), [`MapMarker3D`](sdk-for-android-explore-api-reference-latestmapmarker3d "class in com.here.sdk.mapview") or [`MapImageOverlay`](sdk-for-android-explore-api-reference-latestmapimageoverlay "class in com.here.sdk.mapview") to be shown on the map.
[MapImageFactory](sdk-for-android-explore-api-reference-latestmapimagefactory "class in com.here.sdk.mapview")
Convenience factory class for loading marker resources from various sources.
[MapImageOverlay](sdk-for-android-explore-api-reference-latestmapimageoverlay "class in com.here.sdk.mapview")
`MapImageOverlay` is used to draw images over the map, at a view coordinate inside the map viewport.
[MapItemKeyFrameTrack](sdk-for-android-explore-api-reference-latestmapitemkeyframetrack "class in com.here.sdk.animation")
Stores keyframes for interpolation of a map item property using a specific easing function and interpolation mode.
[MapItemKeyFrameTrack.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapitemkeyframetrack-instantiationerrorcode "enum class in com.here.sdk.animation")
Describes a reason for failing to create a [`MapItemKeyFrameTrack`](sdk-for-android-explore-api-reference-latestmapitemkeyframetrack "class in com.here.sdk.animation").
[MapItemKeyFrameTrack.InstantiationException](sdk-for-android-explore-api-reference-latestmapitemkeyframetrack-instantiationexception "class in com.here.sdk.animation")
Thrown when a problem occurs while trying to create [`MapItemKeyFrameTrack`](sdk-for-android-explore-api-reference-latestmapitemkeyframetrack "class in com.here.sdk.animation").
[MapItemRepresentation](sdk-for-android-explore-api-reference-latestmapitemrepresentation "class in com.here.sdk.mapview")
Base class to represent visual style of particular map items.
[MapLayer](sdk-for-android-explore-api-reference-latestmaplayer "class in com.here.sdk.mapview")
Interface for managing a map layer.
[MapLayerBuilder](sdk-for-android-explore-api-reference-latestmaplayerbuilder "class in com.here.sdk.mapview")
MapLayerBuilder is used to add layers to a map to visualise a dataset in a programmatic way without defining it upfront in the configuration files.
[MapLayerBuilder.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmaplayerbuilder-instantiationerrorcode "enum class in com.here.sdk.mapview")
Describes a reason for failing to build a [`MapLayer`](sdk-for-android-explore-api-reference-latestmaplayer "class in com.here.sdk.mapview").
[MapLayerBuilder.InstantiationErrorDetails](sdk-for-android-explore-api-reference-latestmaplayerbuilder-instantiationerrordetails "class in com.here.sdk.mapview")
Describes the reason for failing to build a [`MapLayer`](sdk-for-android-explore-api-reference-latestmaplayer "class in com.here.sdk.mapview").
[MapLayerBuilder.InstantiationException](sdk-for-android-explore-api-reference-latestmaplayerbuilder-instantiationexception "class in com.here.sdk.mapview")
Thrown when failing to build a [`MapLayer`](sdk-for-android-explore-api-reference-latestmaplayer "class in com.here.sdk.mapview").
[MapLayerMapMeasureDependentStorageLevels](sdk-for-android-explore-api-reference-latestmaplayermapmeasuredependentstoragelevels "class in com.here.sdk.mapview")
Provides a mapping between a MapLayer map measure to datasource storage level.
[MapLayerPriority](sdk-for-android-explore-api-reference-latestmaplayerpriority "class in com.here.sdk.mapview")
MapLayerPriority class.
[MapLayerPriorityBuilder](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder "class in com.here.sdk.mapview")
MapLayerPriorityBuilder is an interface used to define the rendering priority of a layer and its categories, relative to other layers or layer-category pairs.
[MapLayerVisibilityRange](sdk-for-android-explore-api-reference-latestmaplayervisibilityrange "class in com.here.sdk.mapview")
A layer's visibility along a zoom level range.
[MapMarker](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview")
`MapMarker` is used to draw images on the map, for example to mark a specific location.
[MapMarker.TextStyle](sdk-for-android-explore-api-reference-latestmapmarker-textstyle "class in com.here.sdk.mapview")
Styling options for the text of a [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview").
[MapMarker.TextStyle.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-instantiationerrorcode "enum class in com.here.sdk.mapview")
Describes a reason for failing to create a [`MapMarker.TextStyle`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle "class in com.here.sdk.mapview").
[MapMarker.TextStyle.InstantiationException](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-instantiationexception "class in com.here.sdk.mapview")
Thrown when a problem occurs while trying to create a [`MapMarker.TextStyle`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle "class in com.here.sdk.mapview") instance.
[MapMarker.TextStyle.Placement](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview")
Represents text placement with respect to the icon of a [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview").
[MapMarker3D](sdk-for-android-explore-api-reference-latestmapmarker3d "class in com.here.sdk.mapview")
Represents a 3D shape drawn on the map at specified geodetic coordinates.
[MapMarker3DModel](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview")
Represents a 3D model that can be used by a [`MapMarker3D`](sdk-for-android-explore-api-reference-latestmapmarker3d "class in com.here.sdk.mapview") to be shown on the map.
[MapMarker3DModel.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapmarker3dmodel-instantiationerrorcode "enum class in com.here.sdk.mapview")
Indicates the reason for a failure to create [`MapMarker3DModel`](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview").
[MapMarker3DModel.InstantiationException](sdk-for-android-explore-api-reference-latestmapmarker3dmodel-instantiationexception "class in com.here.sdk.mapview")
Thrown when a problem occurs while trying to create [`MapMarker3DModel`](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview").
[MapMarkerAnimation](sdk-for-android-explore-api-reference-latestmapmarkeranimation "class in com.here.sdk.animation")
An animation that can be applied to the [`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview") object.
[MapMarkerAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapmarkeranimation-instantiationerrorcode "enum class in com.here.sdk.animation")
Describes a reason for failing to create a [`MapMarkerAnimation`](sdk-for-android-explore-api-reference-latestmapmarkeranimation "class in com.here.sdk.animation").
[MapMarkerAnimation.InstantiationException](sdk-for-android-explore-api-reference-latestmapmarkeranimation-instantiationexception "class in com.here.sdk.animation")
Thrown when a problem occurs while trying to create a [`MapMarkerAnimation`](sdk-for-android-explore-api-reference-latestmapmarkeranimation "class in com.here.sdk.animation").
[MapMarkerCluster](sdk-for-android-explore-api-reference-latestmapmarkercluster "class in com.here.sdk.mapview")
Groups map markers and enables their clustering to reduce visual clutter when there are many of them in a small area.
[MapMarkerCluster.CounterStyle](sdk-for-android-explore-api-reference-latestmapmarkercluster-counterstyle "class in com.here.sdk.mapview")
Styling options for a marker cluster which is represented by the marker count as a text.
[MapMarkerCluster.Grouping](sdk-for-android-explore-api-reference-latestmapmarkercluster-grouping "class in com.here.sdk.mapview")
Represents a group of map markers belonging to a cluster.
[MapMarkerCluster.ImageStyle](sdk-for-android-explore-api-reference-latestmapmarkercluster-imagestyle "class in com.here.sdk.mapview")
This class specifies the visual appearance of a cluster marker.
[MapMatchedCoordinates](sdk-for-android-explore-api-reference-latestmapmatchedcoordinates "class in com.here.sdk.routing")
Information about the user defined coordinates and where they match to the map.
[MapMeasure](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview")
A map measure.
[MapMeasure.Kind](sdk-for-android-explore-api-reference-latestmapmeasure-kind "enum class in com.here.sdk.mapview")
Kinds of measures.
[MapMeasureDependentRenderSize](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview")
Represents a render size, described as map measure dependent values.
[MapMeasureDependentRenderSize.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize-instantiationerrorcode "enum class in com.here.sdk.mapview")
Describes a reason for failing to create a [`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview").
[MapMeasureDependentRenderSize.InstantiationException](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize-instantiationexception "class in com.here.sdk.mapview")
Thrown when a problem occurs while trying to create [`MapMeasureDependentRenderSize`](sdk-for-android-explore-api-reference-latestmapmeasuredependentrendersize "class in com.here.sdk.mapview").
[MapMeasureRange](sdk-for-android-explore-api-reference-latestmapmeasurerange "class in com.here.sdk.mapview")
A map measure range.
[MapObjectDescriptor](sdk-for-android-explore-api-reference-latestmapobjectdescriptor "class in com.here.sdk.mapview")
Interface represents descriptor of a pickable map object.
[MapPickResult](sdk-for-android-explore-api-reference-latestmappickresult "class in com.here.sdk.mapview")
A class representing a map pick result.
[MapPolygon](sdk-for-android-explore-api-reference-latestmappolygon "class in com.here.sdk.mapview")
A visual representation of a polygon on the map.
[MapPolyline](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview")
A visual representation of a line on the map.
[MapPolyline.DashImageRepresentation](sdk-for-android-explore-api-reference-latestmappolyline-dashimagerepresentation "class in com.here.sdk.mapview")
Represents a dash pattern for the map polyline consisting of images rendered with certain gaps from each other.
[MapPolyline.DashRepresentation](sdk-for-android-explore-api-reference-latestmappolyline-dashrepresentation "class in com.here.sdk.mapview")
Represents a dash pattern for map polyline where the dash can be rendered as a colored line and the gap can be either empty or colored.
[MapPolyline.Representation](sdk-for-android-explore-api-reference-latestmappolyline-representation "class in com.here.sdk.mapview")
Base class to represent the visual appearance of a [`MapPolyline`](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview").
[MapPolyline.Representation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmappolyline-representation-instantiationerrorcode "enum class in com.here.sdk.mapview")
Describes a reason for failing to create a [`MapPolyline.Representation`](sdk-for-android-explore-api-reference-latestmappolyline-representation "class in com.here.sdk.mapview").
[MapPolyline.Representation.InstantiationException](sdk-for-android-explore-api-reference-latestmappolyline-representation-instantiationexception "class in com.here.sdk.mapview")
Thrown when a problem occurs while trying to create [`MapPolyline.Representation`](sdk-for-android-explore-api-reference-latestmappolyline-representation "class in com.here.sdk.mapview").
[MapPolyline.SolidRepresentation](sdk-for-android-explore-api-reference-latestmappolyline-solidrepresentation "class in com.here.sdk.mapview")
Representation for a solid line without outline.
[MapPolylineAnimation](sdk-for-android-explore-api-reference-latestmappolylineanimation "class in com.here.sdk.animation")
An animation that can be applied to the [`MapPolyline`](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview") object.
[MapPolylineAnimation.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmappolylineanimation-instantiationerrorcode "enum class in com.here.sdk.animation")
Describes a reason for failing to create a [`MapPolylineAnimation`](sdk-for-android-explore-api-reference-latestmappolylineanimation "class in com.here.sdk.animation").
[MapPolylineAnimation.InstantiationException](sdk-for-android-explore-api-reference-latestmappolylineanimation-instantiationexception "class in com.here.sdk.animation")
Thrown when a problem occurs while trying to create a [`MapPolylineAnimation`](sdk-for-android-explore-api-reference-latestmappolylineanimation "class in com.here.sdk.animation").
[MapProjection](sdk-for-android-explore-api-reference-latestmapprojection "enum class in com.here.sdk.mapview")
The map projection used for rendering.
[MapRenderMode](sdk-for-android-explore-api-reference-latestmaprendermode "enum class in com.here.sdk.mapview")
Mode of rendering the map by a `MapView`.
[MapScene](sdk-for-android-explore-api-reference-latestmapscene "class in com.here.sdk.mapview")
Represents a map scene and exposes the functionality to manipulate its content.
[MapScene.LoadSceneCallback](sdk-for-android-explore-api-reference-latestmapscene-loadscenecallback "interface in com.here.sdk.mapview")
Called on the main thread after `loadScene()` method finishes loading the scene.
[MapScene.MapPickFilter](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter "class in com.here.sdk.mapview")
Filter for the map content to be picked.
[MapScene.MapPickFilter.ContentType](sdk-for-android-explore-api-reference-latestmapscene-mappickfilter-contenttype "enum class in com.here.sdk.mapview")
Type of the map content to be picked.
[MapSceneLights](sdk-for-android-explore-api-reference-latestmapscenelights "class in com.here.sdk.mapview")
Manage the lights and their attributes in a scene.
[MapSceneLights.AttributeSettingCallback](sdk-for-android-explore-api-reference-latestmapscenelights-attributesettingcallback "interface in com.here.sdk.mapview")
This callback function allows handling errors that occur during the setting of light attributes.
[MapSceneLights.AttributeSettingError](sdk-for-android-explore-api-reference-latestmapscenelights-attributesettingerror "enum class in com.here.sdk.mapview")
Error enum indicating reasons for failure when setting light attributes.
[MapSceneLights.Category](sdk-for-android-explore-api-reference-latestmapscenelights-category "enum class in com.here.sdk.mapview")
The scene uses three categories of lighting which are: Main light, Back light and Rim light.
[MapSceneLights.Direction](sdk-for-android-explore-api-reference-latestmapscenelights-direction "class in com.here.sdk.mapview")
The direction of lights as a pair of azimuth and altitude angles.
[MapSceneLoadOptions](sdk-for-android-explore-api-reference-latestmapsceneloadoptions "class in com.here.sdk.mapview")
Represents the configuration options for loading a map scene.
[MapSceneLoadOptionsBuilder](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder "class in com.here.sdk.mapview")
Builder for creating [`MapSceneLoadOptions`](sdk-for-android-explore-api-reference-latestmapsceneloadoptions "class in com.here.sdk.mapview") instances.
[MapSceneLoadOptionsBuilder.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder-instantiationerrorcode "enum class in com.here.sdk.mapview")
Describes a reason for failing to build a [`MapSceneLoadOptions`](sdk-for-android-explore-api-reference-latestmapsceneloadoptions "class in com.here.sdk.mapview").
[MapSceneLoadOptionsBuilder.InstantiationErrorDetails](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder-instantiationerrordetails "class in com.here.sdk.mapview")
Describes the reason for failing to build a [`MapSceneLoadOptions`](sdk-for-android-explore-api-reference-latestmapsceneloadoptions "class in com.here.sdk.mapview").
[MapSceneLoadOptionsBuilder.InstantiationException](sdk-for-android-explore-api-reference-latestmapsceneloadoptionsbuilder-instantiationexception "class in com.here.sdk.mapview")
Thrown when failing to build a [`MapSceneLoadOptions`](sdk-for-android-explore-api-reference-latestmapsceneloadoptions "class in com.here.sdk.mapview").
[MapScheme](sdk-for-android-explore-api-reference-latestmapscheme "enum class in com.here.sdk.mapview")
Represents the preconfigured map schemes bundled with the SDK.
[MapSurface](sdk-for-android-explore-api-reference-latestmapsurface "class in com.here.sdk.mapview")
Provides the ability to render a map into a provided rendering surface.
[MapSurface.RenderListener](sdk-for-android-explore-api-reference-latestmapsurface-renderlistener "interface in com.here.sdk.mapview")
Listener of MapSurface render events.
[MapView](sdk-for-android-explore-api-reference-latestmapview "class in com.here.sdk.mapview")
A view that can display a map.
[MapView.OnReadyListener](sdk-for-android-explore-api-reference-latestmapview-onreadylistener "interface in com.here.sdk.mapview")
Listener that gets notified when MapView is fully initialized and ready to handle all operations, which means that map scene is loaded and drawing surface is ready to render a map.
[MapView.TakeScreenshotCallback](sdk-for-android-explore-api-reference-latestmapview-takescreenshotcallback "interface in com.here.sdk.mapview")
Callback to be called on retrieval of screenshot.
[MapView.ViewPin](sdk-for-android-explore-api-reference-latestmapview-viewpin "interface in com.here.sdk.mapview")
A ViewPin is used to display Android views at a fixed location on the map.
[MapViewBase](sdk-for-android-explore-api-reference-latestmapviewbase "interface in com.here.sdk.mapview")
Represents the available public API from `MapView`.
[MapViewBase.MapPickCallback](sdk-for-android-explore-api-reference-latestmapviewbase-mappickcallback "interface in com.here.sdk.mapview")
Callback for a pick request.
[MapViewLifecycleListener](sdk-for-android-explore-api-reference-latestmapviewlifecyclelistener "interface in com.here.sdk.mapview")
Provides a mechanism for observing a lifecycle of a map view and/or implementing components whose lifecycle needs to be linked with that of a map view.
[MapViewOptions](sdk-for-android-explore-api-reference-latestmapviewoptions "class in com.here.sdk.mapview")
Options used for initialization of map view
[MatchSideOfStreet](sdk-for-android-explore-api-reference-latestmatchsideofstreet "enum class in com.here.sdk.routing")
Specifies how the location set by [`Waypoint.sideOfStreetHint`](sdk-for-android-explore-api-reference-latestwaypoint#sideOfStreetHint) should be handled.
[MaterialReflectivity](sdk-for-android-explore-api-reference-latestmaterialreflectivity "class in com.here.sdk.mapview")
Material reflectivity properties are used to enable per‑pixel lighting for supported map objects (e.g.
[MaxAxleGroupWeight](sdk-for-android-explore-api-reference-latestmaxaxlegroupweight "class in com.here.sdk.routing")
`MaxAxleGroupWeight` contains all the restriction details violated by an axle group weight.
[MaxSpeedOnSegment](sdk-for-android-explore-api-reference-latestmaxspeedonsegment "class in com.here.sdk.routing")
New base speed for a segment.
[Mesh](sdk-for-android-explore-api-reference-latestmesh "class in com.here.sdk.mapview")
Represents a mesh in 3D space.
[MeshBuilder](sdk-for-android-explore-api-reference-latestmeshbuilder "class in com.here.sdk.mapview")
Builder for meshes.
[Metadata](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core")
Holds metadata on behalf of a map item.
[MetadataType](sdk-for-android-explore-api-reference-latestmetadatatype "enum class in com.here.sdk.core")
Different types of objects that can be stored in a Metadata class instance.
[MobilePhone](sdk-for-android-explore-api-reference-latestmobilephone "class in com.here.sdk.search")
Represents data related to specific mobile phone number.
[NameID](sdk-for-android-explore-api-reference-latestnameid "class in com.here.sdk.core")
Structure to represent name-id pairs.
[NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Internal base class for public non-POD objects to manage the lifecycle of underlying C++ objects.
[NetworkEndpoint](sdk-for-android-explore-api-reference-latestnetworkendpoint "class in com.here.sdk.core")
Network endpoint.
[NetworkSettings](sdk-for-android-explore-api-reference-latestnetworksettings "class in com.here.sdk.core.engine")
Network configuration to be used by [`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") during the initialization.
[NoticeSeverity](sdk-for-android-explore-api-reference-latestnoticeseverity "enum class in com.here.sdk.routing")
Describes the impact a notice has on the resource to which the notice is attached.
[OnTaskCompleted](sdk-for-android-explore-api-reference-latestontaskcompleted "interface in com.here.sdk.core.threading")
The method will be called on the main thread when a task call has been completed.
[OpeningHours](sdk-for-android-explore-api-reference-latestopeninghours "class in com.here.sdk.search")
Represents opening hours information.
[OptimizationMode](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing")
Identifiers for different optimizations that can be used during the route calculation while trying to keep the quality of the route being calculated high.
[PanListener](sdk-for-android-explore-api-reference-latestpanlistener "interface in com.here.sdk.gestures")
Interface for handling pan gestures.
[ParameterConfiguration](sdk-for-android-explore-api-reference-latestparameterconfiguration "class in com.here.sdk.core")
Contains values of configurable parameters that are used in SDK.
[PassThroughFeature](sdk-for-android-explore-api-reference-latestpassthroughfeature "enum class in com.here.sdk.core.engine")
Represents features that are allowed to consume online data when the HERE SDK's offline mode is activated via [`SDKNativeEngine.isOfflineMode()`](sdk-for-android-explore-api-reference-latestsdknativeengine#isOfflineMode()) and/or [`SDKOptions.offlineMode`](sdk-for-android-explore-api-reference-latestsdkoptions#offlineMode).
[PassThroughWaypoint](sdk-for-android-explore-api-reference-latestpassthroughwaypoint "class in com.here.sdk.routing")
This structure provides all the information for a passthrough waypoint.
[PaymentMethod](sdk-for-android-explore-api-reference-latestpaymentmethod "enum class in com.here.sdk.routing")
Available payment methods.
[PedestrianOptions](sdk-for-android-explore-api-reference-latestpedestrianoptions "class in com.here.sdk.routing")
Deprecated.
Will be removed in v4.28.0.
[PedestrianProfile](sdk-for-android-explore-api-reference-latestpedestrianprofile "class in com.here.sdk.core")
Contains values of pedestrian profile.
[PedestrianSpecification](sdk-for-android-explore-api-reference-latestpedestrianspecification "class in com.here.sdk.transport")
Pedestrian specific settings.
[PhysicalConsumptionModel](sdk-for-android-explore-api-reference-latestphysicalconsumptionmodel "class in com.here.sdk.routing")
Defines the physical consumption model for electric vehicles, using vehicle-specific parameters to calculate energy consumption along a route.
[PickedPlace](sdk-for-android-explore-api-reference-latestpickedplace "class in com.here.sdk.core")
Carries the result of picking a Carto POI (point of interest) object.
[PickMapContentResult](sdk-for-android-explore-api-reference-latestpickmapcontentresult "class in com.here.sdk.mapview")
A class that contains possible results from picking map content on the map scene.
[PickMapContentResult.TrafficIncidentResult](sdk-for-android-explore-api-reference-latestpickmapcontentresult-trafficincidentresult "class in com.here.sdk.mapview")
Carries the result of picking a Carto traffic incident object.
[PickMapItemsResult](sdk-for-android-explore-api-reference-latestpickmapitemsresult "class in com.here.sdk.mapview")
Carries results from the picking of map items on the map scene.
[PinchRotateListener](sdk-for-android-explore-api-reference-latestpinchrotatelistener "interface in com.here.sdk.gestures")
Interface for handling pinch rotate gestures.
[Place](sdk-for-android-explore-api-reference-latestplace "class in com.here.sdk.search")
Represents a location object, such as a country, a city, a point of interest (POI) etc.
[PlaceCategory](sdk-for-android-explore-api-reference-latestplacecategory "class in com.here.sdk.search")
Represents a category of place with different levels of granularity.
[PlaceChain](sdk-for-android-explore-api-reference-latestplacechain "class in com.here.sdk.search")
Parameters related to HERE Places chain system.
[PlaceFilter](sdk-for-android-explore-api-reference-latestplacefilter "class in com.here.sdk.search")
The filter options to specify a place.
[PlaceFilter.Ev](sdk-for-android-explore-api-reference-latestplacefilter-ev "class in com.here.sdk.search")
Constraints that are applicable on the places of category EV station.
[PlaceFoodType](sdk-for-android-explore-api-reference-latestplacefoodtype "class in com.here.sdk.search")
Parameters related to HERE Places cuisine system.
[PlaceIdQuery](sdk-for-android-explore-api-reference-latestplaceidquery "class in com.here.sdk.search")
The options to specify a Place id query.
[PlaceIdSearchCallback](sdk-for-android-explore-api-reference-latestplaceidsearchcallback "interface in com.here.sdk.search")
The method will be called on the main thread when a search by id call has been completed.
[PlaceIdSearchCallbackExtended](sdk-for-android-explore-api-reference-latestplaceidsearchcallbackextended "interface in com.here.sdk.search")
The method will be called on the main thread when a search by id call has been completed.
[PlaceSerializationError](sdk-for-android-explore-api-reference-latestplaceserializationerror "enum class in com.here.sdk.search")
Represents and error, which occurs during place serialization and deserialization routines.
[PlaceSerializationException](sdk-for-android-explore-api-reference-latestplaceserializationexception "class in com.here.sdk.search")
Place serialization exception
[PlaceType](sdk-for-android-explore-api-reference-latestplacetype "enum class in com.here.sdk.search")
Specifies place type of Place result from a search query.
[PlatformThreading](sdk-for-android-explore-api-reference-latestplatformthreading "interface in com.here.sdk.core.threading")
Interface for task activities on the main thread.
[Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")
Represents a point in 2D space.
[Point2DKeyframe](sdk-for-android-explore-api-reference-latestpoint2dkeyframe "class in com.here.sdk.animation")
A Point2D keyframe.
[Point3D](sdk-for-android-explore-api-reference-latestpoint3d "class in com.here.sdk.core")
Represents a point in 3D space.
[PointData](sdk-for-android-explore-api-reference-latestpointdata "class in com.here.sdk.mapview.datasource")
Represents a geodetic point with custom attributes.
[PointDataAccessor](sdk-for-android-explore-api-reference-latestpointdataaccessor "class in com.here.sdk.mapview.datasource")
Point data accessor used for manipulating points that are part of a PointDataSource.
[PointDataBuilder](sdk-for-android-explore-api-reference-latestpointdatabuilder "class in com.here.sdk.mapview.datasource")
Builder of [`PointData`](sdk-for-android-explore-api-reference-latestpointdata "class in com.here.sdk.mapview.datasource") instances.
[PointDataSource](sdk-for-android-explore-api-reference-latestpointdatasource "class in com.here.sdk.mapview.datasource")
Point data source allows the rendering engine access to the user provided geographical locations and their attributes.
[PointDataSource.PointDataProcessor](sdk-for-android-explore-api-reference-latestpointdatasource-pointdataprocessor "interface in com.here.sdk.mapview.datasource")
Called for each point, allowing inspection, removal or update of coordinates and attributes.
[PointDataSourceBuilder](sdk-for-android-explore-api-reference-latestpointdatasourcebuilder "class in com.here.sdk.mapview.datasource")
Builder of points data source.
[PointTileDataSource](sdk-for-android-explore-api-reference-latestpointtiledatasource "class in com.here.sdk.mapview.datasource")
Point tile data source allows the rendering engine access to user managed data sets of geographical locations and their attributes through a [`PointTileSource`](sdk-for-android-explore-api-reference-latestpointtilesource "interface in com.here.sdk.mapview.datasource").
[PointTileSource](sdk-for-android-explore-api-reference-latestpointtilesource "interface in com.here.sdk.mapview.datasource")
A source of geodetic point tiles.
[PointTileSource.LoadResultHandler](sdk-for-android-explore-api-reference-latestpointtilesource-loadresulthandler "interface in com.here.sdk.mapview.datasource")
Result handler of a load tile request.
[POIPaymentDetails](sdk-for-android-explore-api-reference-latestpoipaymentdetails "class in com.here.sdk.search")
Details about the payment options at the POI.
[POIPaymentMethod](sdk-for-android-explore-api-reference-latestpoipaymentmethod "class in com.here.sdk.search")
Holds constants that represent payment methods.
[PolygonData](sdk-for-android-explore-api-reference-latestpolygondata "class in com.here.sdk.mapview.datasource")
Represents a geodetic polygon with custom attributes.
[PolygonDataAccessor](sdk-for-android-explore-api-reference-latestpolygondataaccessor "class in com.here.sdk.mapview.datasource")
Polygon data accessor used for manipulating polygons that are part of a PolygonDataSource.
[PolygonDataBuilder](sdk-for-android-explore-api-reference-latestpolygondatabuilder "class in com.here.sdk.mapview.datasource")
Builder of [`PolygonData`](sdk-for-android-explore-api-reference-latestpolygondata "class in com.here.sdk.mapview.datasource") instances.
[PolygonDataSource](sdk-for-android-explore-api-reference-latestpolygondatasource "class in com.here.sdk.mapview.datasource")
Polygon data source allows the rendering engine access to the user provided polygons geometry and their attributes.
[PolygonDataSource.PolygonDataProcessor](sdk-for-android-explore-api-reference-latestpolygondatasource-polygondataprocessor "interface in com.here.sdk.mapview.datasource")
Called for each polygon, allowing inspection, removal or update of coordinates and attributes.
[PolygonDataSourceBuilder](sdk-for-android-explore-api-reference-latestpolygondatasourcebuilder "class in com.here.sdk.mapview.datasource")
Builder of the polygons data source.
[PolygonTileDataSource](sdk-for-android-explore-api-reference-latestpolygontiledatasource "class in com.here.sdk.mapview.datasource")
Polygon tile data source allows the rendering engine access to user managed data sets of geodetic polygons and their attributes through a [`PolygonTileSource`](sdk-for-android-explore-api-reference-latestpolygontilesource "interface in com.here.sdk.mapview.datasource").
[PolygonTileSource](sdk-for-android-explore-api-reference-latestpolygontilesource "interface in com.here.sdk.mapview.datasource")
A source of geodetic polygon tiles.
[PolygonTileSource.LoadResultHandler](sdk-for-android-explore-api-reference-latestpolygontilesource-loadresulthandler "interface in com.here.sdk.mapview.datasource")
Result handler of a load tile request.
[PolylineSimplificationCallback](sdk-for-android-explore-api-reference-latestpolylinesimplificationcallback "interface in com.here.sdk.core")
The method will be called on the main thread when [`PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.GeoCoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)`](sdk-for-android-explore-api-reference-latestpolylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)) is finished.
[PolylineSimplificationError](sdk-for-android-explore-api-reference-latestpolylinesimplificationerror "enum class in com.here.sdk.core")
Error code which specifies, what went wrong during [`PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.GeoCoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)`](sdk-for-android-explore-api-reference-latestpolylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)) operation.
[PolylineSimplifier](sdk-for-android-explore-api-reference-latestpolylinesimplifier "class in com.here.sdk.core")
PolylineSimplifier helps to reduce the number of points in the polyline by removing redundant elements using Douglas–Peucker algorithm, so that result stays within [`PolylineSimplifier.Options`](sdk-for-android-explore-api-reference-latestpolylinesimplifier-options "class in com.here.sdk.core").
[PolylineSimplifier.Options](sdk-for-android-explore-api-reference-latestpolylinesimplifier-options "class in com.here.sdk.core")
Controls the strategy of [`PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.GeoCoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)`](sdk-for-android-explore-api-reference-latestpolylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)) when reducing a size of polyline.
[PostAction](sdk-for-android-explore-api-reference-latestpostaction "class in com.here.sdk.routing")
An action that must be done after arrival, i.e.
[PostActionType](sdk-for-android-explore-api-reference-latestpostactiontype "enum class in com.here.sdk.routing")
Identifies the action type.
[PreAction](sdk-for-android-explore-api-reference-latestpreaction "class in com.here.sdk.routing")
An action that must be done prior to the section, i.e.
[PreActionType](sdk-for-android-explore-api-reference-latestpreactiontype "enum class in com.here.sdk.routing")
Identifies the action type.
[PrivateBusOptions](sdk-for-android-explore-api-reference-latestprivatebusoptions "class in com.here.sdk.routing")
Deprecated.
Will be removed in v4.28.0.
[ProxySettings](sdk-for-android-explore-api-reference-latestproxysettings "class in com.here.sdk.core.engine")
Proxy configuration for the HERE SDK network that is applied per request.
[ProxySettings.Credentials](sdk-for-android-explore-api-reference-latestproxysettings-credentials "class in com.here.sdk.core.engine")
Authentication data
[ProxySettings.ProxyType](sdk-for-android-explore-api-reference-latestproxysettings-proxytype "enum class in com.here.sdk.core.engine")
Supported types of proxy connection.
[QuadMeshBuilder](sdk-for-android-explore-api-reference-latestquadmeshbuilder "class in com.here.sdk.mapview")
Builder for a single quad.
[RasterDataSource](sdk-for-android-explore-api-reference-latestrasterdatasource "class in com.here.sdk.mapview.datasource")
Data source to load map layers using a raster image format (jpg, png).
[RasterDataSourceConfiguration](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration "class in com.here.sdk.mapview.datasource")
Called on the main thread after `fromJsonFile()` method finishes loading the configuration.
[RasterDataSourceConfiguration.Cache](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration-cache "class in com.here.sdk.mapview.datasource")
Configuration of a local data cache.
[RasterDataSourceConfiguration.Provider](sdk-for-android-explore-api-reference-latestrasterdatasourceconfiguration-provider "class in com.here.sdk.mapview.datasource")
Configuration of a data provider.
[RasterDataSourceConfigurationUpdate](sdk-for-android-explore-api-reference-latestrasterdatasourceconfigurationupdate "class in com.here.sdk.mapview.datasource")
Configuration update for a RasterDataSource.
[RasterDataSourceError](sdk-for-android-explore-api-reference-latestrasterdatasourceerror "enum class in com.here.sdk.mapview.datasource")
Raster data source error codes.
[RasterDataSourceListener](sdk-for-android-explore-api-reference-latestrasterdatasourcelistener "interface in com.here.sdk.mapview.datasource")
Listener for RasterDataSource events.
[RasterTileSource](sdk-for-android-explore-api-reference-latestrastertilesource "interface in com.here.sdk.mapview.datasource")
A source of raster tiles.
[RasterTileSource.LoadResultHandler](sdk-for-android-explore-api-reference-latestrastertilesource-loadresulthandler "interface in com.here.sdk.mapview.datasource")
Result handler of a load tile request.
[Rectangle2D](sdk-for-android-explore-api-reference-latestrectangle2d "class in com.here.sdk.core")
Represents a 2D rectangle defined by the origin and size.
[RefreshRouteOptions](sdk-for-android-explore-api-reference-latestrefreshrouteoptions "class in com.here.sdk.routing")
Deprecated.
Will be removed in v4.28.0.
[RenderSize](sdk-for-android-explore-api-reference-latestrendersize "class in com.here.sdk.mapview")
Represents size of visual elements drawn on the map.
[RenderSize.Unit](sdk-for-android-explore-api-reference-latestrendersize-unit "enum class in com.here.sdk.mapview")
Defines different units in which the size is described.
[ResponseDetails](sdk-for-android-explore-api-reference-latestresponsedetails "class in com.here.sdk.search")
Structure holding various information received with response to a query.
[RoadFeatures](sdk-for-android-explore-api-reference-latestroadfeatures "enum class in com.here.sdk.routing")
Road features or states.
[RoadShieldIconProperties](sdk-for-android-explore-api-reference-latestroadshieldiconproperties "class in com.here.sdk.mapview")
Contains the information required to create a road shield image.
[RoadTexts](sdk-for-android-explore-api-reference-latestroadtexts "class in com.here.sdk.routing")
Textual attributes of road.
[Route](sdk-for-android-explore-api-reference-latestroute "class in com.here.sdk.routing")
A route is a path through a road network over which someone travels.
[RouteHandle](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing")
Provides an opaque handle to the calculated [`Route`](sdk-for-android-explore-api-reference-latestroute "class in com.here.sdk.routing").
[RouteLabel](sdk-for-android-explore-api-reference-latestroutelabel "class in com.here.sdk.routing")
The main street name or road number for a route.
[RouteLabelType](sdk-for-android-explore-api-reference-latestroutelabeltype "enum class in com.here.sdk.routing")
Identifies the type of the route label.
[RouteOffset](sdk-for-android-explore-api-reference-latestrouteoffset "class in com.here.sdk.routing")
Represents a specific location along the route.
[RouteOptions](sdk-for-android-explore-api-reference-latestrouteoptions "class in com.here.sdk.routing")
The options to specify how the route will be calculated.
[RoutePlace](sdk-for-android-explore-api-reference-latestrouteplace "class in com.here.sdk.routing")
The location information.
[RoutePlaceDirection](sdk-for-android-explore-api-reference-latestrouteplacedirection "enum class in com.here.sdk.routing")
Specifies the direction to make distinction between departure and arrival cases.
[RoutePlaceType](sdk-for-android-explore-api-reference-latestrouteplacetype "enum class in com.here.sdk.routing")
Identifies the route place type.
[RouteRailwayCrossing](sdk-for-android-explore-api-reference-latestrouterailwaycrossing "class in com.here.sdk.routing")
Contains information about railway crossing.
[RouteRailwayCrossingType](sdk-for-android-explore-api-reference-latestrouterailwaycrossingtype "enum class in com.here.sdk.routing")
Identify possible type of route railway crossing.
[RouteStop](sdk-for-android-explore-api-reference-latestroutestop "class in com.here.sdk.routing")
Route stop that should be used together with import route functionality.
[RouteTextOptions](sdk-for-android-explore-api-reference-latestroutetextoptions "class in com.here.sdk.routing")
Specify how textual output should be provided.
[RouteType](sdk-for-android-explore-api-reference-latestroutetype "enum class in com.here.sdk.core")
Indicates the level of significance of a route in a range from 1 to 6.
[RoutingConnectionSettings](sdk-for-android-explore-api-reference-latestroutingconnectionsettings "class in com.here.sdk.routing")
Defines the settings for the retry logic when connecting to the HERE routing backend.
[RoutingEngine](sdk-for-android-explore-api-reference-latestroutingengine "class in com.here.sdk.routing")
Use the RoutingEngine to calculate a route from A to B with a number of waypoints in between.
[RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing")
Specifies possible errors that may result from the calculation of a route.
[RoutingInterface](sdk-for-android-explore-api-reference-latestroutinginterface "interface in com.here.sdk.routing")
Provides the interface for the online and offline routing engines.
[RoutingOptions](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing")
The options defines how a route should be calculated.
[Runnable](sdk-for-android-explore-api-reference-latestrunnable "interface in com.here.sdk.core.threading")
Interface that should be implemented by any class whose instances are intended to be executed by a thread.
[ScalarKeyframe](sdk-for-android-explore-api-reference-latestscalarkeyframe "class in com.here.sdk.animation")
A ScalarKeyframe consists of a scalar value (e.g,: distance in meters) and an animation duration.
[ScaleHandler](sdk-for-android-explore-api-reference-latestscalehandler "class in com.here.sdk.gestures")
This class handles scale events by zooming the map accordingly.
[ScheduleDetails](sdk-for-android-explore-api-reference-latestscheduledetails "class in com.here.sdk.search")
Encapsulates schedule details complying with the iCalendar specification: https://tools.ietf.org/html/rfc5545.
[ScooterOptions](sdk-for-android-explore-api-reference-latestscooteroptions "class in com.here.sdk.routing")
Deprecated.
Will be removed in v4.28.0.
[ScooterSpecification](sdk-for-android-explore-api-reference-latestscooterspecification "class in com.here.sdk.transport")
Scooter specific settings.
[ScrollHandler](sdk-for-android-explore-api-reference-latestscrollhandler "class in com.here.sdk.gestures")
This class handles scroll events by panning the map accordingly.
[SDKBuildInformation](sdk-for-android-explore-api-reference-latestsdkbuildinformation "class in com.here.sdk.core.engine")
The SDKBuildInformation class is designed to provide information about the SDK build.
[SDKLibraryLoader](sdk-for-android-explore-api-reference-latestsdklibraryloader "class in com.here.sdk.core")
Loads HERE SDK native libraries.
[SDKLogger](sdk-for-android-explore-api-reference-latestsdklogger "class in com.here.sdk.core.engine")
Logging interface for Android/iOS platforms.
[SDKNativeEngine](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine")
Holds internal services and configurations needed by various HERE SDK modules.
[SDKNativeEngine.PurgeMemoryStrategy](sdk-for-android-explore-api-reference-latestsdknativeengine-purgememorystrategy "enum class in com.here.sdk.core.engine")
Enum representing a strategy to flush memory caches.
[SDKOptions](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine")
SDKOptions provide an alternative way to set or update the HERE SDK credentials and other parameters at runtime to initialize the [`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine").
[SDKOptions.ActionOnCacheLock](sdk-for-android-explore-api-reference-latestsdkoptions-actiononcachelock "enum class in com.here.sdk.core.engine")
Action on cache lock
[SDKVersion](sdk-for-android-explore-api-reference-latestsdkversion "class in com.here.sdk.core.engine")
The `SDKVersion` represents version information for an SDK product.
[SearchCallback](sdk-for-android-explore-api-reference-latestsearchcallback "interface in com.here.sdk.search")
The method will be called on the main thread when a search call has been completed.
[SearchCallbackExtended](sdk-for-android-explore-api-reference-latestsearchcallbackextended "interface in com.here.sdk.search")
The method will be called on the main thread when a search call has been completed.
[SearchEngine](sdk-for-android-explore-api-reference-latestsearchengine "class in com.here.sdk.search")
The SearchEngine API unlocks the search, geocoding and suggesting capabilities of HERE services to provide developers with unmatched flexibility to create differentiating location-enabled applications.
[SearchError](sdk-for-android-explore-api-reference-latestsearcherror "enum class in com.here.sdk.search")
Specifies possible errors that may result from a search query.
[SearchInterface](sdk-for-android-explore-api-reference-latestsearchinterface "interface in com.here.sdk.search")
Provides the interface for the online and offline search engines.
[SearchOptions](sdk-for-android-explore-api-reference-latestsearchoptions "class in com.here.sdk.search")
Encapsulates options that control the behavior of search and suggest operations.
[Section](sdk-for-android-explore-api-reference-latestsection "class in com.here.sdk.routing")
A section is a part of the route between two stopovers.
[SectionNotice](sdk-for-android-explore-api-reference-latestsectionnotice "class in com.here.sdk.routing")
Explains an issue encountered in a [`Section`](sdk-for-android-explore-api-reference-latestsection "class in com.here.sdk.routing").
[SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing")
Notice codes which point the issues encountered during processing of a [`Section`](sdk-for-android-explore-api-reference-latestsection "class in com.here.sdk.routing").
[SectionTransportMode](sdk-for-android-explore-api-reference-latestsectiontransportmode "enum class in com.here.sdk.routing")
Specifies the [`Section`](sdk-for-android-explore-api-reference-latestsection "class in com.here.sdk.routing") mode of transport.
[SegmentReference](sdk-for-android-explore-api-reference-latestsegmentreference "class in com.here.sdk.routing")
Reference to a segment id with a travel direction.
[ShadowQuality](sdk-for-android-explore-api-reference-latestshadowquality "enum class in com.here.sdk.mapview")
The shadow quality.
[SideOfDestination](sdk-for-android-explore-api-reference-latestsideofdestination "enum class in com.here.sdk.routing")
Specifies the side of street on which the destination is located.
[Signpost](sdk-for-android-explore-api-reference-latestsignpost "class in com.here.sdk.routing")
Signpost information.
[SignpostLabel](sdk-for-android-explore-api-reference-latestsignpostlabel "class in com.here.sdk.routing")
Details of a signpost representing a particular direction or destination.
[Size2D](sdk-for-android-explore-api-reference-latestsize2d "class in com.here.sdk.core")
Represents the size of a 2D structure.
[Span](sdk-for-android-explore-api-reference-latestspan "class in com.here.sdk.routing")
A span is a part of the [`Section`](sdk-for-android-explore-api-reference-latestsection "class in com.here.sdk.routing") which is traversable or navigable.
[StreetAttributes](sdk-for-android-explore-api-reference-lateststreetattributes "enum class in com.here.sdk.routing")
Types of street attributes.
[StructuredQuery](sdk-for-android-explore-api-reference-lateststructuredquery "class in com.here.sdk.search")
The options to specify a structured query.
[StructuredQuery.AddressElements](sdk-for-android-explore-api-reference-lateststructuredquery-addresselements "class in com.here.sdk.search")
Defines query address elements which will be used to build address hierarchy during searches.
[StructuredQuery.ResultType](sdk-for-android-explore-api-reference-lateststructuredquery-resulttype "enum class in com.here.sdk.search")
Specifies expected result type.
[Style](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview")
A style that defines the visual appearance of map rendered features.
[SuggestCallback](sdk-for-android-explore-api-reference-latestsuggestcallback "interface in com.here.sdk.search")
The method will be called on the main thread when a suggest call has been completed.
[SuggestCallbackExtended](sdk-for-android-explore-api-reference-latestsuggestcallbackextended "interface in com.here.sdk.search")
The method will be called on the main thread when a suggest call has been completed.
[Suggestion](sdk-for-android-explore-api-reference-latestsuggestion "class in com.here.sdk.search")
Suggestion is meant to provide relevant suggestions to partial queries, like "restaur", "starbu", "eiffel".
[SuggestionType](sdk-for-android-explore-api-reference-latestsuggestiontype "enum class in com.here.sdk.search")
Specifies the type of suggestion returned for query.
[SupplierReference](sdk-for-android-explore-api-reference-latestsupplierreference "class in com.here.sdk.search")
Identifier of the place as provided by the supplier
[TapListener](sdk-for-android-explore-api-reference-latesttaplistener "interface in com.here.sdk.gestures")
Interface for handling tap gestures.
[TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")
Handle used for the manipulation of the task.
[TaskOutcome](sdk-for-android-explore-api-reference-latesttaskoutcome "enum class in com.here.sdk.core.threading")
This enum represents that a task has been completed.
[TaxiOptions](sdk-for-android-explore-api-reference-latesttaxioptions "class in com.here.sdk.routing")
Deprecated.
Will be removed in v4.28.0.
[TaxiSpecification](sdk-for-android-explore-api-reference-latesttaxispecification "class in com.here.sdk.transport")
Taxi specific settings.
[TextQuery](sdk-for-android-explore-api-reference-latesttextquery "class in com.here.sdk.search")
The options to specify a text query.
[TextQuery.Area](sdk-for-android-explore-api-reference-latesttextquery-area "class in com.here.sdk.search")
Area to perform search on.
[TextUsageOptions](sdk-for-android-explore-api-reference-latesttextusageoptions "class in com.here.sdk.routing")
Specify whether the text should be used when generating notification.
[Threading](sdk-for-android-explore-api-reference-latestthreading "class in com.here.sdk.core.threading")
Initializes threading support on native side.
[TileGeoBoundsCalculator](sdk-for-android-explore-api-reference-latesttilegeoboundscalculator "class in com.here.sdk.mapview.datasource")
A calculator of geodetic bounds for tiles identified by keys generated in a particular tiling scheme ([`TilingScheme`](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource")).
[TileKey](sdk-for-android-explore-api-reference-latesttilekey "class in com.here.sdk.mapview.datasource")
Key of a data source tile.
[TileSource](sdk-for-android-explore-api-reference-latesttilesource "interface in com.here.sdk.mapview.datasource")
A source of tiles.
[TileSource.DataVersion](sdk-for-android-explore-api-reference-latesttilesource-dataversion "class in com.here.sdk.mapview.datasource")
Tile data version.
[TileSource.Listener](sdk-for-android-explore-api-reference-latesttilesource-listener "interface in com.here.sdk.mapview.datasource")
Listener of [`TileSource`](sdk-for-android-explore-api-reference-latesttilesource "interface in com.here.sdk.mapview.datasource") events.
[TileSource.LoadTileRequestHandle](sdk-for-android-explore-api-reference-latesttilesource-loadtilerequesthandle "interface in com.here.sdk.mapview.datasource")
Handle of a load request.
[TileSource.TileMetadata](sdk-for-android-explore-api-reference-latesttilesource-tilemetadata "class in com.here.sdk.mapview.datasource")
Tile metadata.
[TileUrlProviderCallback](sdk-for-android-explore-api-reference-latesttileurlprovidercallback "interface in com.here.sdk.mapview.datasource")
Provides the URL as String for the given tile coordinates and storage level.
[TileUrlProviderFactory](sdk-for-android-explore-api-reference-latesttileurlproviderfactory "class in com.here.sdk.mapview.datasource")
Factory for generating a [`TileUrlProviderCallback`](sdk-for-android-explore-api-reference-latesttileurlprovidercallback "interface in com.here.sdk.mapview.datasource") utilized in creating a tile URL.
[TilingScheme](sdk-for-android-explore-api-reference-latesttilingscheme "enum class in com.here.sdk.mapview.datasource")
List of available data tiling schemes.
[TimeRule](sdk-for-android-explore-api-reference-latesttimerule "class in com.here.sdk.core")
Used to indicate a time period of one or more intervals in [GDF](https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/concepts/time-domain.html) specification.
[Toll](sdk-for-android-explore-api-reference-latesttoll "class in com.here.sdk.routing")
This struct presents all the data for a toll.
[TollFare](sdk-for-android-explore-api-reference-latesttollfare "class in com.here.sdk.routing")
This struct presents all the fare data for a toll.
[TollFarePass](sdk-for-android-explore-api-reference-latesttollfarepass "class in com.here.sdk.routing")
[`TollFare`](sdk-for-android-explore-api-reference-latesttollfare "class in com.here.sdk.routing") multi-travel pass characteristics.
[TollOptions](sdk-for-android-explore-api-reference-latesttolloptions "class in com.here.sdk.routing")
The option to specify how the tolls should be calculated.
[TollOptions.EmissionType](sdk-for-android-explore-api-reference-latesttolloptions-emissiontype "enum class in com.here.sdk.routing")
Supported options of emission type
[TollOptions.VehicleCategory](sdk-for-android-explore-api-reference-latesttolloptions-vehiclecategory "enum class in com.here.sdk.routing")
Supported options of vehicle category for toll calculation.
[TrafficDataProvider](sdk-for-android-explore-api-reference-latesttrafficdataprovider "class in com.here.sdk.traffic")
This interface provides traffic information from radio signals to other HERE SDK modules.
[TrafficEngine](sdk-for-android-explore-api-reference-latesttrafficengine "class in com.here.sdk.traffic")
Use the TrafficEngine to get information about current traffic flow and incidents in an area specified by [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core"), [`GeoCircle`](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core"), or [`GeoCorridor`](sdk-for-android-explore-api-reference-latestgeocorridor "class in com.here.sdk.core").
[TrafficFlow](sdk-for-android-explore-api-reference-latesttrafficflow "class in com.here.sdk.traffic")
This class provides details about traffic flow along a [`GeoCorridor`](sdk-for-android-explore-api-reference-latestgeocorridor "class in com.here.sdk.core"), inside a [`GeoCircle`](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core") or a [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core"), that represents particular path of the road network.
Backends for TrafficEngine and traffic vector tiles are different however backends may share the same data.
For additional information about fields, refer to [Traffic API v7 API Reference: Traffic API v7](https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic).
[TrafficFlowBase](sdk-for-android-explore-api-reference-latesttrafficflowbase "interface in com.here.sdk.traffic")
This interface provides details about a traffic flow.
For additional information about fields, refer to [Traffic API v7 API Reference: Traffic API v7](https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic).
[TrafficFlowQueryCallback](sdk-for-android-explore-api-reference-latesttrafficflowquerycallback "interface in com.here.sdk.traffic")
Callback passed to following functions: [`TrafficEngine.queryForFlow(GeoBox, TrafficFlowQueryOptions, TrafficFlowQueryCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#queryForFlow(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback)) [`TrafficEngine.queryForFlow(GeoCircle, TrafficFlowQueryOptions, TrafficFlowQueryCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#queryForFlow(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback)) [`TrafficEngine.queryForFlow(GeoCorridor, TrafficFlowQueryOptions, TrafficFlowQueryCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#queryForFlow(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback)) The method will be called on the main thread when a search call has been completed.
[TrafficFlowQueryOptions](sdk-for-android-explore-api-reference-latesttrafficflowqueryoptions "class in com.here.sdk.traffic")
The options to specify how traffic flow data should be queried.
[TrafficIncident](sdk-for-android-explore-api-reference-latesttrafficincident "class in com.here.sdk.traffic")
TrafficIncident provides details about a traffic incident.
[TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")
The vehicle categories that can be restricted.
[TrafficIncident.VehicleRestriction](sdk-for-android-explore-api-reference-latesttrafficincident-vehiclerestriction "class in com.here.sdk.traffic")
The vehicle restriction representing a vehicle category and relevant restriction rules.
[TrafficIncidentBase](sdk-for-android-explore-api-reference-latesttrafficincidentbase "interface in com.here.sdk.traffic")
TrafficIncident provides details about a traffic incident.
[TrafficIncidentImpact](sdk-for-android-explore-api-reference-latesttrafficincidentimpact "enum class in com.here.sdk.traffic")
Impact of a traffic incident.
[TrafficIncidentLookupCallback](sdk-for-android-explore-api-reference-latesttrafficincidentlookupcallback "interface in com.here.sdk.traffic")
Callback passed to [`TrafficEngine.lookupIncident(java.lang.String, com.here.sdk.traffic.TrafficIncidentLookupOptions, com.here.sdk.traffic.TrafficIncidentLookupCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#lookupIncident(java.lang.String,com.here.sdk.traffic.TrafficIncidentLookupOptions,com.here.sdk.traffic.TrafficIncidentLookupCallback)).
[TrafficIncidentLookupOptions](sdk-for-android-explore-api-reference-latesttrafficincidentlookupoptions "class in com.here.sdk.traffic")
All the options to specify how a single incident should be queried.
[TrafficIncidentOnRoute](sdk-for-android-explore-api-reference-latesttrafficincidentonroute "class in com.here.sdk.routing")
Traffic incidents on a route.
[TrafficIncidentsQueryCallback](sdk-for-android-explore-api-reference-latesttrafficincidentsquerycallback "interface in com.here.sdk.traffic")
Callback passed to [`TrafficEngine.queryForIncidents(GeoCorridor, TrafficIncidentsQueryOptions, TrafficIncidentsQueryCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#queryForIncidents(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficIncidentsQueryOptions,com.here.sdk.traffic.TrafficIncidentsQueryCallback)).
[TrafficIncidentsQueryOptions](sdk-for-android-explore-api-reference-latesttrafficincidentsqueryoptions "class in com.here.sdk.traffic")
The options to specify how incidents should be queried.
[TrafficIncidentType](sdk-for-android-explore-api-reference-latesttrafficincidenttype "enum class in com.here.sdk.traffic")
Category of a traffic incident.
[TrafficLocation](sdk-for-android-explore-api-reference-latesttrafficlocation "class in com.here.sdk.traffic")
The location reference to the traffic incident.
[TrafficOnRoute](sdk-for-android-explore-api-reference-latesttrafficonroute "class in com.here.sdk.routing")
Traffic information on a route.
[TrafficOnSection](sdk-for-android-explore-api-reference-latesttrafficonsection "class in com.here.sdk.routing")
Traffic information on a section.
[TrafficOnSpan](sdk-for-android-explore-api-reference-latesttrafficonspan "class in com.here.sdk.routing")
Traffic information of a span along a route.
[TrafficOptimizationMode](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode "enum class in com.here.sdk.routing")
Traffic optimization mode that defines whether and what kind of traffic information should be considered during route calculation.
[TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic")
Represents various errors that could occur from a traffic queries.
[TransitDeparture](sdk-for-android-explore-api-reference-latesttransitdeparture "class in com.here.sdk.routing")
This struct holds the transit departure or arrival information.
[TransitDepartureStatus](sdk-for-android-explore-api-reference-latesttransitdeparturestatus "enum class in com.here.sdk.routing")
Status of a departure.
[TransitIncident](sdk-for-android-explore-api-reference-latesttransitincident "class in com.here.sdk.routing")
A transit incident describes disruptions on the transit network.
[TransitIncidentEffect](sdk-for-android-explore-api-reference-latesttransitincidenteffect "enum class in com.here.sdk.routing")
Transit incident effect.
[TransitIncidentType](sdk-for-android-explore-api-reference-latesttransitincidenttype "enum class in com.here.sdk.routing")
Transit incident type.
[TransitMode](sdk-for-android-explore-api-reference-latesttransitmode "enum class in com.here.sdk.routing")
Public transit mode
[TransitModeFilter](sdk-for-android-explore-api-reference-latesttransitmodefilter "enum class in com.here.sdk.routing")
Filtering mode for public transit.
[TransitRouteOptions](sdk-for-android-explore-api-reference-latesttransitrouteoptions "class in com.here.sdk.routing")
All the options to specify how a public transit route should be calculated.
[TransitRoutingEngine](sdk-for-android-explore-api-reference-latesttransitroutingengine "class in com.here.sdk.routing")
Use the TransitRoutingEngine to calculate a public transit route from A to B with a number of waypoints in between.
[TransitSectionDetails](sdk-for-android-explore-api-reference-latesttransitsectiondetails "class in com.here.sdk.routing")
Gives the details of a transit section.
[TransitStop](sdk-for-android-explore-api-reference-latesttransitstop "class in com.here.sdk.routing")
A transit stop between the departure and destination of a transit section.
[TransitTransport](sdk-for-android-explore-api-reference-latesttransittransport "class in com.here.sdk.routing")
Holds all the transit transport information.
[TransitWaypoint](sdk-for-android-explore-api-reference-latesttransitwaypoint "class in com.here.sdk.routing")
Represents a transit waypoint, used as input for transit route calculation.
[TranslucentMapLayerGroup](sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup "class in com.here.sdk.mapview")
A translucent layer group that can be the target for [`MapLayerPriorityBuilder.inGroup(java.lang.String)`](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder#inGroup(java.lang.String)).
[TranslucentMapLayerGroup.ErrorCode](sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup-errorcode "enum class in com.here.sdk.mapview")
Error codes for creating the group.
[TranslucentMapLayerGroup.ErrorDetails](sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup-errordetails "class in com.here.sdk.mapview")
Describes the reason for failing to create the group.
[TranslucentMapLayerGroup.InstantiationException](sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup-instantiationexception "class in com.here.sdk.mapview")
Thrown when failing to build the group.
[TransportMode](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport")
Specifies the mode of transport used for route calculalation.
[TransportProfile](sdk-for-android-explore-api-reference-latesttransportprofile "class in com.here.sdk.core")
Contains values of transport profile.
[TransportSpecification](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport")
Contains transport attributes details related to the transport mode.
[TransportSpecification.BicycleBuilder](sdk-for-android-explore-api-reference-latesttransportspecification-bicyclebuilder "class in com.here.sdk.transport")
This class constructs a [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") for a bicycle.
[TransportSpecification.BusBuilder](sdk-for-android-explore-api-reference-latesttransportspecification-busbuilder "class in com.here.sdk.transport")
This class constructs a [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") for a bus.
[TransportSpecification.CarBuilder](sdk-for-android-explore-api-reference-latesttransportspecification-carbuilder "class in com.here.sdk.transport")
This class constructs a [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") for a car.
[TransportSpecification.PedestrianBuilder](sdk-for-android-explore-api-reference-latesttransportspecification-pedestrianbuilder "class in com.here.sdk.transport")
This class constructs a [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") for pedestrian.
[TransportSpecification.PrivateBusBuilder](sdk-for-android-explore-api-reference-latesttransportspecification-privatebusbuilder "class in com.here.sdk.transport")
This class constructs a [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") for a private bus.
[TransportSpecification.ScooterBuilder](sdk-for-android-explore-api-reference-latesttransportspecification-scooterbuilder "class in com.here.sdk.transport")
This class constructs a [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") for a scooter.
[TransportSpecification.TaxiBuilder](sdk-for-android-explore-api-reference-latesttransportspecification-taxibuilder "class in com.here.sdk.transport")
This class constructs a [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") for a taxi.
[TransportSpecification.TruckBuilder](sdk-for-android-explore-api-reference-latesttransportspecification-truckbuilder "class in com.here.sdk.transport")
This class constructs a [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") for a truck.
[TravelDirection](sdk-for-android-explore-api-reference-latesttraveldirection "enum class in com.here.sdk.routing")
Travel direction.
[Traversability](sdk-for-android-explore-api-reference-latesttraversability "enum class in com.here.sdk.traffic")
Junctions traversability of some traffic incident or flow section.
[TriangleMeshBuilder](sdk-for-android-explore-api-reference-latesttrianglemeshbuilder "class in com.here.sdk.mapview")
Builder for a single triangle.
[TruckAmenities](sdk-for-android-explore-api-reference-latesttruckamenities "class in com.here.sdk.search")
Truck amenities struct, represents availability (true/false) for each feature, except shower_count - number of showers, if data is available.
[TruckCategory](sdk-for-android-explore-api-reference-latesttruckcategory "enum class in com.here.sdk.transport")
Specifies the truck category.
[TruckClass](sdk-for-android-explore-api-reference-latesttruckclass "enum class in com.here.sdk.transport")
Defines truck class based on weight.
[TruckFuel](sdk-for-android-explore-api-reference-latesttruckfuel "class in com.here.sdk.search")
Contains truck fuel type info of fuel station.
[TruckFuelType](sdk-for-android-explore-api-reference-latesttruckfueltype "enum class in com.here.sdk.transport")
Define possible fuel types for trucks provided by a fuel station.
[TruckOptions](sdk-for-android-explore-api-reference-latesttruckoptions "class in com.here.sdk.routing")
Deprecated.
Will be removed in v4.28.0.
[TruckRoadType](sdk-for-android-explore-api-reference-latesttruckroadtype "enum class in com.here.sdk.transport")
Specifies Truck road type
[TruckSpecifications](sdk-for-android-explore-api-reference-latesttruckspecifications "class in com.here.sdk.transport")
Truck specifications contain vehicle related attributes.
[TruckType](sdk-for-android-explore-api-reference-latesttrucktype "enum class in com.here.sdk.transport")
Deprecated.
Will be removed in v4.27.0.
[TunnelCategory](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport")
Specifies the tunnel categories.
[TwoFingerPanListener](sdk-for-android-explore-api-reference-latesttwofingerpanlistener "interface in com.here.sdk.gestures")
Interface for handling two finger pan gestures.
[TwoFingerTapListener](sdk-for-android-explore-api-reference-latesttwofingertaplistener "interface in com.here.sdk.gestures")
Interface for handling two finger tap gestures.
[UnitSystem](sdk-for-android-explore-api-reference-latestunitsystem "enum class in com.here.sdk.core")
Represents the available unit systems(imperial/metric).
[UsageStats](sdk-for-android-explore-api-reference-latestusagestats "class in com.here.sdk.core.engine")
A class that gathers statistics of the HERE SDK network usage for uploaded and downloaded data.
[UsageStats.Feature](sdk-for-android-explore-api-reference-latestusagestats-feature "enum class in com.here.sdk.core.engine")
Represents the feature enum associated with the gathered usage stats.
[UsageStats.NetworkStats](sdk-for-android-explore-api-reference-latestusagestats-networkstats "class in com.here.sdk.core.engine")
Provides network statistics in bytes per method.
[VehicleProfile](sdk-for-android-explore-api-reference-latestvehicleprofile "class in com.here.sdk.transport")
A vehicle profile describes the vehicle being used with the HSDK.
[VehicleRestrictionMaxWeight](sdk-for-android-explore-api-reference-latestvehiclerestrictionmaxweight "class in com.here.sdk.routing")
`VehicleRestrictionMaxWeight` contains max permitted weight during the trip, in kilograms, along with the specific type of maximum permitted weight restriction.
[VehicleRestrictionMaxWeightType](sdk-for-android-explore-api-reference-latestvehiclerestrictionmaxweighttype "enum class in com.here.sdk.routing")
This enum represents the specific type of the maximum permitted weight restriction.
[VehicleSpecification](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport")
Contains vehicle related attributes.
[VehicleSpecification.BusBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-busbuilder "class in com.here.sdk.transport")
This class constructs a [`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") for a bus.
[VehicleSpecification.CarBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-carbuilder "class in com.here.sdk.transport")
This class constructs a [`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") for a car.
[VehicleSpecification.PrivateBusBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport")
This class constructs a [`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") for a private bus.
[VehicleSpecification.ScooterBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-scooterbuilder "class in com.here.sdk.transport")
This class constructs a [`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") for a scooter.
[VehicleSpecification.TaxiBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-taxibuilder "class in com.here.sdk.transport")
This class constructs a [`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") for a taxi.
[VehicleSpecification.TruckBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-truckbuilder "class in com.here.sdk.transport")
This class constructs a [`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") for a truck.
[VehicleType](sdk-for-android-explore-api-reference-latestvehicletype "enum class in com.here.sdk.transport")
Defines the type of the vehicle.
[ViolatedRestriction](sdk-for-android-explore-api-reference-latestviolatedrestriction "class in com.here.sdk.routing")
`ViolatedRestriction` contains all the violated restriction details for the planned trip.
[ViolatedRestriction.Details](sdk-for-android-explore-api-reference-latestviolatedrestriction-details "class in com.here.sdk.routing")
Optional restriction details, contains additional information depending on the specific violation, zero or more member might be set.
[VisibilityState](sdk-for-android-explore-api-reference-latestvisibilitystate "enum class in com.here.sdk.mapview")
Represents the visibility state of an SDK map view's object.
[WalkAttributes](sdk-for-android-explore-api-reference-latestwalkattributes "enum class in com.here.sdk.routing")
Types of walk attributes.
[WatermarkStyle](sdk-for-android-explore-api-reference-latestwatermarkstyle "enum class in com.here.sdk.mapview")
Defines the style of the HERE watermark logo.
[Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")
Represents a waypoint, used as input for route calculation.
[WaypointType](sdk-for-android-explore-api-reference-latestwaypointtype "enum class in com.here.sdk.routing")
Defines if the waypoint is a stop over, or a hint for a desired polyline of a route.
[WebDetails](sdk-for-android-explore-api-reference-latestwebdetails "class in com.here.sdk.search")
Contains information about images, editorials, rating and a urls to them.
[WebEditorial](sdk-for-android-explore-api-reference-latestwebeditorial "class in com.here.sdk.search")
Contains information about editorial article and a link to it.
[WebImage](sdk-for-android-explore-api-reference-latestwebimage "class in com.here.sdk.search")
Contains image information and direct link to it.
[WebRating](sdk-for-android-explore-api-reference-latestwebrating "class in com.here.sdk.search")
Contains information about rating and a url to review.
[WebsiteAddress](sdk-for-android-explore-api-reference-latestwebsiteaddress "class in com.here.sdk.search")
Represents data related to specific website address
[WebSource](sdk-for-android-explore-api-reference-latestwebsource "class in com.here.sdk.search")
Contains information about provider of the item and a direct link to the item.
[WeightPerAxleGroup](sdk-for-android-explore-api-reference-latestweightperaxlegroup "class in com.here.sdk.transport")
Struct which defines the weight of the different axle groups of a vehicle.
[ZoneCategory](sdk-for-android-explore-api-reference-latestzonecategory "enum class in com.here.sdk.routing")
Identifies categories of zones which routes avoid going through when used in [`AvoidanceOptions`](sdk-for-android-explore-api-reference-latestavoidanceoptions "class in com.here.sdk.routing").
