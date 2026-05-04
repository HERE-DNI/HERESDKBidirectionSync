---
title: "com.here.sdk.core (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpackage-summary"
hidden: false
---

# Package com.here.sdk.core

------------------------------------------------------------------------
package com.here.sdk.core

Related Packages

Package

  Description

  [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

  [com.here.sdk.core.errors](sdk-for-android-explore-api-reference-latestpackage-summary)

  [com.here.sdk.core.threading](sdk-for-android-explore-api-reference-latestpackage-summary)

  [com.here.sdk.core.utilities](sdk-for-android-explore-api-reference-latestpackage-summary)

All Classes and Interfaces
  Interfaces
  Classes
  Enum Classes
  Exceptions

  Class

  Description

  [Anchor2D](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core")

Represents a point in a rectangle as a ratio of this rectangle's width and height.

[Angle](sdk-for-android-explore-api-reference-latestangle "class in com.here.sdk.core")

Represents an angle independent of the unit of measurement.

[AngleRange](sdk-for-android-explore-api-reference-latestanglerange "class in com.here.sdk.core")

Represents angle ranges as a circular sector by using an absolute start angle and a relative range angle called extent.

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

[CardinalDirection](sdk-for-android-explore-api-reference-latestcardinaldirection "enum class in com.here.sdk.core")

Indicates the official directional identifier assigned to this road.

[Color](sdk-for-android-explore-api-reference-latestcolor "class in com.here.sdk.core")

Represents a color value.

[CountryCode](sdk-for-android-explore-api-reference-latestcountrycode "enum class in com.here.sdk.core")

This enum represents country codes in accordance with the ISO 3166-1 standard using alpha-3 codes.

[CurrentType](sdk-for-android-explore-api-reference-latestcurrenttype "enum class in com.here.sdk.core")

This enum represents the type of electric current

[CustomMetadataValue](sdk-for-android-explore-api-reference-latestcustommetadatavalue "interface in com.here.sdk.core")

Interface for storing arbitrary metadata types.

[ExternalID](sdk-for-android-explore-api-reference-latestexternalid "class in com.here.sdk.core")

Identifier of the entity as provided by the external source

[GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")

Represents a bounding rectangle aligned with latitude and longitude.

[GeoCircle](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core")

Represents a circle area in 2D space.

[GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

Represents geographical coordinates in 3D space.

[GeoCoordinatesUpdate](sdk-for-android-explore-api-reference-latestgeocoordinatesupdate "class in com.here.sdk.core")

Represents geographical coordinates in 3D space.

[GeoCorridor](sdk-for-android-explore-api-reference-latestgeocorridor "class in com.here.sdk.core")

A geographical area that wraps around a geographical polyline with a given distance.

[GeoOrientation](sdk-for-android-explore-api-reference-latestgeoorientation "class in com.here.sdk.core")

Geodetic orientation with bearing, tilt and roll.

[GeoOrientationUpdate](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core")

Describes geodetic orientation update with bearing and tilt.

[GeoPolygon](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core")

Represents a `GeoPolygon` area as a series of geographic coordinates, and optionally, a list of inner boundaries (also known as holes).

[GeoPolyline](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core")

A list of geographic coordinates representing the vertices of a polyline.

[GeoPolylineDirection](sdk-for-android-explore-api-reference-latestgeopolylinedirection "enum class in com.here.sdk.core")

Defines if a function on a [`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core") computes the operation starting from the beginning or from the end of [`GeoPolyline.vertices`](sdk-for-android-explore-api-reference-latestgeopolyline#vertices).

[IntegerRange](sdk-for-android-explore-api-reference-latestintegerrange "class in com.here.sdk.core")

An integer range \[min, max\] with inclusive minimum and maximum value.

[LanguageCode](sdk-for-android-explore-api-reference-latestlanguagecode "enum class in com.here.sdk.core")

This enum represents language codes.

[LocalizedText](sdk-for-android-explore-api-reference-latestlocalizedtext "class in com.here.sdk.core")

Used to represent text localized to specific language.

[LocalizedTexts](sdk-for-android-explore-api-reference-latestlocalizedtexts "class in com.here.sdk.core")

The list of multiple names or titles for the same entity, possibly in different languages.

[Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")

Describes a location in the world at a given time.

[LocationListener](sdk-for-android-explore-api-reference-latestlocationlistener "interface in com.here.sdk.core")

This interface should be implemented in order to receive notifications about location updates.

[LocationSource](sdk-for-android-explore-api-reference-latestlocationsource "enum class in com.here.sdk.core")

Indicates where the location was computed.

[LocationTechnology](sdk-for-android-explore-api-reference-latestlocationtechnology "enum class in com.here.sdk.core")

Technology or provider of the location.

[LocationTime](sdk-for-android-explore-api-reference-latestlocationtime "class in com.here.sdk.core")

This struct presents all the time data tied to a location, like an arrival or departure time.

[Metadata](sdk-for-android-explore-api-reference-latestmetadata "class in com.here.sdk.core")

Holds metadata on behalf of a map item.

[MetadataType](sdk-for-android-explore-api-reference-latestmetadatatype "enum class in com.here.sdk.core")

Different types of objects that can be stored in a Metadata class instance.

[NameID](sdk-for-android-explore-api-reference-latestnameid "class in com.here.sdk.core")

Structure to represent name-id pairs.

[NetworkEndpoint](sdk-for-android-explore-api-reference-latestnetworkendpoint "class in com.here.sdk.core")

Network endpoint.

[ParameterConfiguration](sdk-for-android-explore-api-reference-latestparameterconfiguration "class in com.here.sdk.core")

Contains values of configurable parameters that are used in SDK.

[PedestrianProfile](sdk-for-android-explore-api-reference-latestpedestrianprofile "class in com.here.sdk.core")

Contains values of pedestrian profile.

[PickedPlace](sdk-for-android-explore-api-reference-latestpickedplace "class in com.here.sdk.core")

Carries the result of picking a Carto POI (point of interest) object.

[Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")

Represents a point in 2D space.

[Point3D](sdk-for-android-explore-api-reference-latestpoint3d "class in com.here.sdk.core")

Represents a point in 3D space.

[PolylineSimplificationCallback](sdk-for-android-explore-api-reference-latestpolylinesimplificationcallback "interface in com.here.sdk.core")

The method will be called on the main thread when [`PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.GeoCoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)`](sdk-for-android-explore-api-reference-latestpolylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)) is finished.

[PolylineSimplificationError](sdk-for-android-explore-api-reference-latestpolylinesimplificationerror "enum class in com.here.sdk.core")

Error code which specifies, what went wrong during [`PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.GeoCoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)`](sdk-for-android-explore-api-reference-latestpolylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)) operation.

[PolylineSimplifier](sdk-for-android-explore-api-reference-latestpolylinesimplifier "class in com.here.sdk.core")

PolylineSimplifier helps to reduce the number of points in the polyline by removing redundant elements using Douglas–Peucker algorithm, so that result stays within [`PolylineSimplifier.Options`](sdk-for-android-explore-api-reference-latestpolylinesimplifier-options "class in com.here.sdk.core").

[PolylineSimplifier.Options](sdk-for-android-explore-api-reference-latestpolylinesimplifier-options "class in com.here.sdk.core")

Controls the strategy of [`PolylineSimplifier.simplify(java.util.List<com.here.sdk.core.GeoCoordinates>, com.here.sdk.core.PolylineSimplifier.Options, com.here.sdk.core.PolylineSimplificationCallback)`](sdk-for-android-explore-api-reference-latestpolylinesimplifier#simplify(java.util.List,com.here.sdk.core.PolylineSimplifier.Options,com.here.sdk.core.PolylineSimplificationCallback)) when reducing a size of polyline.

[Rectangle2D](sdk-for-android-explore-api-reference-latestrectangle2d "class in com.here.sdk.core")

Represents a 2D rectangle defined by the origin and size.

[RouteType](sdk-for-android-explore-api-reference-latestroutetype "enum class in com.here.sdk.core")

Indicates the level of significance of a route in a range from 1 to 6.

[SDKLibraryLoader](sdk-for-android-explore-api-reference-latestsdklibraryloader "class in com.here.sdk.core")

Loads HERE SDK native libraries.

[Size2D](sdk-for-android-explore-api-reference-latestsize2d "class in com.here.sdk.core")

Represents the size of a 2D structure.

[TimeRule](sdk-for-android-explore-api-reference-latesttimerule "class in com.here.sdk.core")

Used to indicate a time period of one or more intervals in [GDF](https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/concepts/time-domain.html) specification.

[TransportProfile](sdk-for-android-explore-api-reference-latesttransportprofile "class in com.here.sdk.core")

Contains values of transport profile.

[UnitSystem](sdk-for-android-explore-api-reference-latestunitsystem "enum class in com.here.sdk.core")

Represents the available unit systems(imperial/metric).
