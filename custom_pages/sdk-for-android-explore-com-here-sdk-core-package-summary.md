---
title: "com.here.sdk.core (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-package-summary"
---

<div class="package-signature">

package <span class="element-name">com.here.sdk.core</span>

</div>

<div class="section summary">

- <div id="related-package-summary">

  <div class="caption">

  Related Packages

  </div>

  | Package | Description |
  |----|----|
  | [com.here.sdk.core.engine](sdk-for-android-explore-com-here-sdk-core-engine-package-summary) |   |
  | [com.here.sdk.core.errors](sdk-for-android-explore-com-here-sdk-core-errors-package-summary) |   |
  | [com.here.sdk.core.threading](sdk-for-android-explore-com-here-sdk-core-threading-package-summary) |   |
  | [com.here.sdk.core.utilities](sdk-for-android-explore-com-here-sdk-core-utilities-package-summary) |   |

  </div>

- <div id="class-summary">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Classes and Interfaces
  Interfaces
  Classes
  Enum Classes
  Exceptions

  </div>

  <div id="class-summary.tabpanel" aria-labelledby="class-summary-tab0"
  role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th>Class</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-anchor2d"
  title="class in com.here.sdk.core">Anchor2D</a></td>
  <td><div class="block">
  Represents a point in a rectangle as a ratio of this rectangle's width
  and height.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-angle"
  title="class in com.here.sdk.core">Angle</a></td>
  <td><div class="block">
  Represents an angle independent of the unit of measurement.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-anglerange"
  title="class in com.here.sdk.core">AngleRange</a></td>
  <td><div class="block">
  Represents angle ranges as a circular sector by using an absolute start
  angle and a relative range angle called extent.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-authentication"
  title="class in com.here.sdk.core">Authentication</a></td>
  <td><div class="block">
  Use the authentication class to authenticate and retrieve a secure token
  that can be used with other HERE services.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-authenticationcallback"
  title="interface in com.here.sdk.core">AuthenticationCallback</a></td>
  <td><div class="block">
  Callback passed to Authentication.authenticate(SDKNativeEngine) .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-authenticationdata"
  title="class in com.here.sdk.core">AuthenticationData</a></td>
  <td><div class="block">
  Authentication data
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-authenticationerror"
  title="enum class in com.here.sdk.core">AuthenticationError</a></td>
  <td><div class="block">
  Authentication error
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-authenticationexception"
  title="class in com.here.sdk.core">AuthenticationException</a></td>
  <td><div class="block">
  Authentication exception
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-brandlogo"
  title="class in com.here.sdk.core">BrandLogo</a></td>
  <td><div class="block">
  Represents image link to the company's logo.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-cardinaldirection"
  title="enum class in com.here.sdk.core">CardinalDirection</a></td>
  <td><div class="block">
  Indicates the official directional identifier assigned to this road.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-color"
  title="class in com.here.sdk.core">Color</a></td>
  <td><div class="block">
  Represents a color value.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-countrycode"
  title="enum class in com.here.sdk.core">CountryCode</a></td>
  <td><div class="block">
  This enum represents country codes in accordance with the ISO 3166-1
  standard using alpha-3 codes.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-currenttype"
  title="enum class in com.here.sdk.core">CurrentType</a></td>
  <td><div class="block">
  This enum represents the type of electric current
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-custommetadatavalue"
  title="interface in com.here.sdk.core">CustomMetadataValue</a></td>
  <td><div class="block">
  Interface for storing arbitrary metadata types.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-externalid"
  title="class in com.here.sdk.core">ExternalID</a></td>
  <td><div class="block">
  Identifier of the entity as provided by the external source
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geobox"
  title="class in com.here.sdk.core">GeoBox</a></td>
  <td><div class="block">
  Represents a bounding rectangle aligned with latitude and longitude.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geocircle"
  title="class in com.here.sdk.core">GeoCircle</a></td>
  <td><div class="block">
  Represents a circle area in 2D space.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates"
  title="class in com.here.sdk.core">GeoCoordinates</a></td>
  <td><div class="block">
  Represents geographical coordinates in 3D space.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-geocoordinatesupdate"
  title="class in com.here.sdk.core">GeoCoordinatesUpdate</a></td>
  <td><div class="block">
  Represents geographical coordinates in 3D space.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geocorridor"
  title="class in com.here.sdk.core">GeoCorridor</a></td>
  <td><div class="block">
  A geographical area that wraps around a geographical polyline with a
  given distance.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geoorientation"
  title="class in com.here.sdk.core">GeoOrientation</a></td>
  <td><div class="block">
  Geodetic orientation with bearing, tilt and roll.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-geoorientationupdate"
  title="class in com.here.sdk.core">GeoOrientationUpdate</a></td>
  <td><div class="block">
  Describes geodetic orientation update with bearing and tilt.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geopolygon"
  title="class in com.here.sdk.core">GeoPolygon</a></td>
  <td><div class="block">
  Represents a GeoPolygon area as a series of geographic coordinates, and
  optionally, a list of inner boundaries (also known as holes).
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geopolyline"
  title="class in com.here.sdk.core">GeoPolyline</a></td>
  <td><div class="block">
  A list of geographic coordinates representing the vertices of a
  polyline.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-geopolylinedirection"
  title="enum class in com.here.sdk.core">GeoPolylineDirection</a></td>
  <td><div class="block">
  Defines if a function on a GeoPolyline computes the operation starting
  from the beginning or from the end of GeoPolyline.vertices .
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-integerrange"
  title="class in com.here.sdk.core">IntegerRange</a></td>
  <td><div class="block">
  An integer range [min, max] with inclusive minimum and maximum value.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-languagecode"
  title="enum class in com.here.sdk.core">LanguageCode</a></td>
  <td><div class="block">
  This enum represents language codes.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-localizedtext"
  title="class in com.here.sdk.core">LocalizedText</a></td>
  <td><div class="block">
  Used to represent text localized to specific language.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-localizedtexts"
  title="class in com.here.sdk.core">LocalizedTexts</a></td>
  <td><div class="block">
  The list of multiple names or titles for the same entity, possibly in
  different languages.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-location"
  title="class in com.here.sdk.core">Location</a></td>
  <td><div class="block">
  Describes a location in the world at a given time.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-locationlistener"
  title="interface in com.here.sdk.core">LocationListener</a></td>
  <td><div class="block">
  This interface should be implemented in order to receive notifications
  about location updates.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-locationsource"
  title="enum class in com.here.sdk.core">LocationSource</a></td>
  <td><div class="block">
  Indicates where the location was computed.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-locationtechnology"
  title="enum class in com.here.sdk.core">LocationTechnology</a></td>
  <td><div class="block">
  Technology or provider of the location.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-locationtime"
  title="class in com.here.sdk.core">LocationTime</a></td>
  <td><div class="block">
  This struct presents all the time data tied to a location, like an
  arrival or departure time.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-metadata"
  title="class in com.here.sdk.core">Metadata</a></td>
  <td><div class="block">
  Holds metadata on behalf of a map item.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-metadatatype"
  title="enum class in com.here.sdk.core">MetadataType</a></td>
  <td><div class="block">
  Different types of objects that can be stored in a Metadata class
  instance.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-nameid"
  title="class in com.here.sdk.core">NameID</a></td>
  <td><div class="block">
  Structure to represent name-id pairs.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-networkendpoint"
  title="class in com.here.sdk.core">NetworkEndpoint</a></td>
  <td><div class="block">
  Network endpoint.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-parameterconfiguration"
  title="class in com.here.sdk.core">ParameterConfiguration</a></td>
  <td><div class="block">
  Contains values of configurable parameters that are used in SDK.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-pedestrianprofile"
  title="class in com.here.sdk.core">PedestrianProfile</a></td>
  <td>Deprecated.
  <div class="deprecation-comment">
  Will be removed in v4.28.0.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-pickedplace"
  title="class in com.here.sdk.core">PickedPlace</a></td>
  <td><div class="block">
  Carries the result of picking a Carto POI (point of interest) object.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-point2d"
  title="class in com.here.sdk.core">Point2D</a></td>
  <td><div class="block">
  Represents a point in 2D space.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-point3d"
  title="class in com.here.sdk.core">Point3D</a></td>
  <td><div class="block">
  Represents a point in 3D space.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-polylinesimplificationcallback"
  title="interface in com.here.sdk.core">PolylineSimplificationCallback</a></td>
  <td><div class="block">
  The method will be called on the main thread when
  PolylineSimplifier.simplify(java.util.List ,
  com.here.sdk.core.PolylineSimplifier.Options,
  com.here.sdk.core.PolylineSimplificationCallback) is finished.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-polylinesimplificationerror"
  title="enum class in com.here.sdk.core">PolylineSimplificationError</a></td>
  <td><div class="block">
  Error code which specifies, what went wrong during
  PolylineSimplifier.simplify(java.util.List ,
  com.here.sdk.core.PolylineSimplifier.Options,
  com.here.sdk.core.PolylineSimplificationCallback) operation.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier"
  title="class in com.here.sdk.core">PolylineSimplifier</a></td>
  <td><div class="block">
  PolylineSimplifier helps to reduce the number of points in the polyline
  by removing redundant elements using Douglas–Peucker algorithm, so that
  result stays within PolylineSimplifier.Options .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-polylinesimplifier-options"
  title="class in com.here.sdk.core">PolylineSimplifier.Options</a></td>
  <td><div class="block">
  Controls the strategy of PolylineSimplifier.simplify(java.util.List ,
  com.here.sdk.core.PolylineSimplifier.Options,
  com.here.sdk.core.PolylineSimplificationCallback) when reducing a size
  of polyline.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-powertype"
  title="enum class in com.here.sdk.core">PowerType</a></td>
  <td><div class="block">
  Represents the type of electrical power.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-rectangle2d"
  title="class in com.here.sdk.core">Rectangle2D</a></td>
  <td><div class="block">
  Represents a 2D rectangle defined by the origin and size.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-routetype"
  title="enum class in com.here.sdk.core">RouteType</a></td>
  <td><div class="block">
  Indicates the level of significance of a route in a range from 1 to 6.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-sdklibraryloader"
  title="class in com.here.sdk.core">SDKLibraryLoader</a></td>
  <td><div class="block">
  Loads HERE SDK native libraries.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-size2d"
  title="class in com.here.sdk.core">Size2D</a></td>
  <td><div class="block">
  Represents the size of a 2D structure.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-timerule"
  title="class in com.here.sdk.core">TimeRule</a></td>
  <td><div class="block">
  Used to indicate a time period of one or more intervals in GDF
  specification.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-transportprofile"
  title="class in com.here.sdk.core">TransportProfile</a></td>
  <td>Deprecated.
  <div class="deprecation-comment">
  Will be removed in v4.28.0.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-unitsystem"
  title="enum class in com.here.sdk.core">UnitSystem</a></td>
  <td><div class="block">
  Represents the available unit systems(imperial/metric).
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

</div>

