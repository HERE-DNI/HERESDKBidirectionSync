---
title: "Place Class Reference"
slug: "sdk-for-ios-navigate-classes-place"
---

# Place

<div class="declaration">

<div class="language">

``` highlight
public class Place
```

``` highlight
extension Place: NativeBase
```

``` highlight
extension Place: Hashable
```

</div>

</div>

Represents a location object, such as a country, a city, a point of interest (POI) etc.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk5PlaceC5titleSSvp"></span>` `<span id="//apple_ref/swift/Property/title" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-place#/s:7heresdk5PlaceC5titleSSvp" class="token"><code>title</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The localized title for the resource.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var title: String { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk5PlaceC2idSSvp"></span>` `<span id="//apple_ref/swift/Property/id" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-place#/s:7heresdk5PlaceC2idSSvp" class="token"><code>id</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The unique id of this resource. It can be used to query further information. When returned from <a href="sdk-for-ios-navigate-classes-offlinesearchengine">`OfflineSearchEngine`</a>, `id` is valid only for `Place` objects whose `place_type` is `POI`. Otherwise, it is empty.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var id: String { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk5PlaceC9placeTypeAA0bD0Ovp"></span>` `<span id="//apple_ref/swift/Property/placeType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-place#/s:7heresdk5PlaceC9placeTypeAA0bD0Ovp" class="token"><code>placeType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The place type.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var placeType: PlaceType { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk5PlaceC8areaTypeAA04AreaD0OSgvp"></span>` `<span id="//apple_ref/swift/Property/areaType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-place#/s:7heresdk5PlaceC8areaTypeAA04AreaD0OSgvp" class="token"><code>areaType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The area type. It is available only when the <a href="sdk-for-ios-navigate-classes-place#/s:7heresdk5PlaceC9placeTypeAA0bD0Ovp">`Place.placeType`</a> is <a href="sdk-for-ios-navigate-enums-placetype#/s:7heresdk9PlaceTypeO4areayA2CmF">`PlaceType.area`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var areaType: AreaType? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk5PlaceC7addressAA7AddressVvp"></span>` `<span id="//apple_ref/swift/Property/address" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-place#/s:7heresdk5PlaceC7addressAA7AddressVvp" class="token"><code>address</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The address of the place.

  Note that while `OfflineSearchEngine.suggest` and `OfflineSearchEngine.suggestByText` set all available details, `SearchEngine.suggest` and `SearchEngine.suggestByText` set only <a href="sdk-for-ios-navigate-structs-address#/s:7heresdk7AddressV11addressTextSSvp">`Address.addressText`</a>. Complete address details can be obtained by searching with <a href="sdk-for-ios-navigate-structs-placeidquery">`PlaceIdQuery`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var address: Address { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk5PlaceC7detailsAA7DetailsVvp"></span>` `<span id="//apple_ref/swift/Property/details" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-place#/s:7heresdk5PlaceC7detailsAA7DetailsVvp" class="token"><code>details</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The place’s detailed information.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var details: Details { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk5PlaceC14geoCoordinatesAA03GeoD0VSgvp"></span>` `<span id="//apple_ref/swift/Property/geoCoordinates" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-place#/s:7heresdk5PlaceC14geoCoordinatesAA03GeoD0VSgvp" class="token"><code>geoCoordinates</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The geographic coordinates of the place. Can be `nil` when retrieved from a suggestion’s place property.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var geoCoordinates: GeoCoordinates? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk5PlaceC25isCoordinatesInterpolatedSbvp"></span>` `<span id="//apple_ref/swift/Property/isCoordinatesInterpolated" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-place#/s:7heresdk5PlaceC25isCoordinatesInterpolatedSbvp" class="token"><code>isCoordinatesInterpolated</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A property that says whether the coordinates of the house number were interpolated or not. This property is valid only for house number results retrieved using online search. When false, it means <a href="sdk-for-ios-navigate-classes-place#/s:7heresdk5PlaceC14geoCoordinatesAA03GeoD0VSgvp">`Place.geoCoordinates`</a> point to an accurate position of the house. Otherwise coordinates are slightly less accurate, but are based on a highly optimized interpolation algorithm.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isCoordinatesInterpolated: Bool { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk5PlaceC12accessPointsSayAA14GeoCoordinatesVGvp"></span>` `<span id="//apple_ref/swift/Property/accessPoints" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-place#/s:7heresdk5PlaceC12accessPointsSayAA14GeoCoordinatesVGvp" class="token"><code>accessPoints</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The access points to the place, such as the points on a road or in a parking lot. A place can have multiple access points. For example, a large warehouse can have multiple entrances, while the center of the warehouse may not be directly reachable. Note that access points are meant to be reachable by vehicles. For routes it is recommended to navigate to one of the available access points (if any), whereas the `sideOfStreetHint` should be set to the geographic coordinates of the place. The list is empty when no access points are known or when the place is directly reachable. A place can have multiple access points. For example, a large warehouse can have multiple entrances, while the center of the warehouse may not be directly reachable. Note that access points are meant to be reachable by vehicles. For routes it is recommended to navigate to one of the available access points (if any), whereas the `sideOfStreetHint` should be set to the geographic coordinates of the place. The list is empty when no access points are known or when the place is directly reachable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var accessPoints: [GeoCoordinates] { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk5PlaceC11boundingBoxAA03GeoD0VSgvp"></span>` `<span id="//apple_ref/swift/Property/boundingBox" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-place#/s:7heresdk5PlaceC11boundingBoxAA03GeoD0VSgvp" class="token"><code>boundingBox</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The geographic coordinates of the map bounding box containing the place.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var boundingBox: GeoBox? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk5PlaceC16distanceInMeterss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/distanceInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-place#/s:7heresdk5PlaceC16distanceInMeterss5Int32VSgvp" class="token"><code>distanceInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The distance from the search center to the place in meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceInMeters: Int32? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk5PlaceC13politicalViewSSSgvp"></span>` `<span id="//apple_ref/swift/Property/politicalView" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-place#/s:7heresdk5PlaceC13politicalViewSSSgvp" class="token"><code>politicalView</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The geopolitical view, defined as a three letter country code, each disputed territory has international and alternative views. Populated when the geopolitical view parameter is set in the <a href="sdk-for-ios-navigate-structs-sdkoptions">`SDKOptions`</a> and passed to <a href="sdk-for-ios-navigate-classes-sdknativeengine">`SDKNativeEngine`</a> on instantiation, but only if it is an alternative view. For more details refer to <a href="sdk-for-ios-navigate-structs-sdkoptions">`SDKOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var politicalView: String? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      serializeCompact()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Serializes `Place` to persist or transfer. Preserves limited amount of data:

  - <a href="sdk-for-ios-navigate-classes-place#/s:7heresdk5PlaceC5titleSSvp">`Place.title`</a>

  - <a href="sdk-for-ios-navigate-classes-place#/s:7heresdk5PlaceC2idSSvp">`Place.id`</a>

  - <a href="sdk-for-ios-navigate-classes-place#/s:7heresdk5PlaceC14geoCoordinatesAA03GeoD0VSgvp">`Place.geoCoordinates`</a>

  - <a href="sdk-for-ios-navigate-classes-place#/s:7heresdk5PlaceC12accessPointsSayAA14GeoCoordinatesVGvp">`Place.accessPoints`</a>

  - <a href="sdk-for-ios-navigate-classes-place#/s:7heresdk5PlaceC9placeTypeAA0bD0Ovp">`Place.placeType`</a>

  - <a href="sdk-for-ios-navigate-classes-place#/s:7heresdk5PlaceC11boundingBoxAA03GeoD0VSgvp">`Place.boundingBox`</a>

  -     Details.getPrimaryCategories(...)

  - <a href="sdk-for-ios-navigate-structs-address#/s:7heresdk7AddressV11addressTextSSvp">`Address.addressText`</a>

  - <a href="sdk-for-ios-navigate-structs-address#/s:7heresdk7AddressV11countryCodeSSvp">`Address.countryCode`</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func serializeCompact () -> String
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  The serialized place

  </div>

  </div>

  </div>

- <div>

      deserialize(serializedPlace: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns a `Place` created from serialized string.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-search#/s:7heresdk27PlaceSerializationExceptiona">`PlaceSerializationException`</a> Indicates what went wrong during deserialization attempt.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func deserialize ( serializedPlace : String ) throws -> Place
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>serializedPlace</code></em><code> </code></td>
  <td><div>
  <p>The serialized place</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  A `Place` created from serialized string.

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

