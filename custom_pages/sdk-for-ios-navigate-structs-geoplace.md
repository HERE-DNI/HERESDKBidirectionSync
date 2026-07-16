---
title: "GeoPlace Structure Reference"
slug: "sdk-for-ios-navigate-structs-geoplace"
---

# GeoPlace

<div class="declaration">

<div class="language">

``` highlight
public struct GeoPlace : Hashable
```

</div>

</div>

GeoPlace struct represents a location object: such as a country, a city, a point of interest (POI) etc. It can be used for PersonalPlace creation, in order to provide search on custom places.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8GeoPlaceV5titleSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-title" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geoplace#sdk-for-ios-navigate-s-7heresdk8GeoPlaceV5titleSSvp" class="token"><code>title</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The localized title for the resource. Note: This String can be empty when no data is available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var title: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8GeoPlaceV11externalIDsSayAA10ExternalIDVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-externalIDs" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geoplace#sdk-for-ios-navigate-s-7heresdk8GeoPlaceV11externalIDsSayAA10ExternalIDVGvp" class="token"><code>externalIDs</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Allows the client to set the id in their own system. The list of supplier references to this place. The references are provided by external suppliers and are only available to users with valid contracts with said suppliers. If the user has no such contracts, the list is empty.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var externalIDs: [ExternalID]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-externalid">ExternalID</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8GeoPlaceV4typeAA0C4TypeOvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-type" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geoplace#sdk-for-ios-navigate-s-7heresdk8GeoPlaceV4typeAA0C4TypeOvp" class="token"><code>type</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies place type.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var type: PlaceType
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-placetype">PlaceType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8GeoPlaceV10categoriesSayAA0C8CategoryCGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-categories" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geoplace#sdk-for-ios-navigate-s-7heresdk8GeoPlaceV10categoriesSayAA0C8CategoryCGvp" class="token"><code>categories</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of corresponding categories Note: This list can be empty when no data is available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var categories: [PlaceCategory]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-placecategory">PlaceCategory</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8GeoPlaceV7addressAA7AddressVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-address" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geoplace#sdk-for-ios-navigate-s-7heresdk8GeoPlaceV7addressAA7AddressVvp" class="token"><code>address</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Address of the place Note: Address can have default value when no data is available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var address: Address
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-address">Address</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8GeoPlaceV8locationAA15LocationDetailsVSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-location" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geoplace#sdk-for-ios-navigate-s-7heresdk8GeoPlaceV8locationAA15LocationDetailsVSgvp" class="token"><code>location</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Geographical details Note: Can be `nil` when retrieved from a suggestion’s place property.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var location: LocationDetails?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-locationdetails">LocationDetails</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8GeoPlaceV8businessAA15BusinessDetailsVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-business" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geoplace#sdk-for-ios-navigate-s-7heresdk8GeoPlaceV8businessAA15BusinessDetailsVvp" class="token"><code>business</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Business details Note: BusinessDetails can have default value when no data is available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var business: BusinessDetails
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-businessdetails">BusinessDetails</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8GeoPlaceV3webAA10WebDetailsVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-web" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geoplace#sdk-for-ios-navigate-s-7heresdk8GeoPlaceV3webAA10WebDetailsVvp" class="token"><code>web</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains info and direct web links to corresponding items. Note: WebDetails can have default value when no data is available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var web: WebDetails
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-webdetails">WebDetails</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8GeoPlaceV5title11externalIDs4type10categories7address8location8business3webACSS_SayAA10ExternalIDVGAA0C4TypeOSayAA0C8CategoryCGAA7AddressVAA15LocationDetailsVSgAA08BusinessS0VAA03WebS0Vtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-title-externalIDs-type-categories-address-location-business-web" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geoplace#sdk-for-ios-navigate-s-7heresdk8GeoPlaceV5title11externalIDs4type10categories7address8location8business3webACSS_SayAA10ExternalIDVGAA0C4TypeOSayAA0C8CategoryCGAA7AddressVAA15LocationDetailsVSgAA08BusinessS0VAA03WebS0Vtcfc" class="token"><code>init(title:</code><wbr></wbr><code>externalIDs:</code><wbr></wbr><code>type:</code><wbr></wbr><code>categories:</code><wbr></wbr><code>address:</code><wbr></wbr><code>location:</code><wbr></wbr><code>business:</code><wbr></wbr><code>web:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(title: String = "", externalIDs: [ExternalID] = [], type: PlaceType = PlaceType.unknown, categories: [PlaceCategory] = [], address: Address = Address(), location: LocationDetails? = nil, business: BusinessDetails = BusinessDetails(), web: WebDetails = WebDetails())
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-externalid">ExternalID</a>
  - <a href="sdk-for-ios-navigate-enums-placetype">PlaceType</a>
  - <a href="sdk-for-ios-navigate-classes-placecategory">PlaceCategory</a>
  - <a href="sdk-for-ios-navigate-structs-address">Address</a>
  - <a href="sdk-for-ios-navigate-structs-locationdetails">LocationDetails</a>
  - <a href="sdk-for-ios-navigate-structs-businessdetails">BusinessDetails</a>
  - <a href="sdk-for-ios-navigate-structs-webdetails">WebDetails</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8GeoPlaceV06makeMyC05title11coordinatesACSS_AA0B11CoordinatesVtFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-makeMyPlace-title-coordinates" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geoplace#sdk-for-ios-navigate-s-7heresdk8GeoPlaceV06makeMyC05title11coordinatesACSS_AA0B11CoordinatesVtFZ" class="token"><code>makeMyPlace(title:</code><wbr></wbr><code>coordinates:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class. All other properties will keep their default value and all properties containing lists will contain empty lists.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func makeMyPlace(title: String, coordinates: GeoCoordinates) -> GeoPlace
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a>

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
  <td><code> </code><em><code>title</code></em><code> </code></td>
  <td><div>
  <p>The title.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>coordinates</code></em><code> </code></td>
  <td><div>
  <p>The coordinates.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  An instance of `GeoPlace`.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8GeoPlaceV5getIDSSyF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getID" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geoplace#sdk-for-ios-navigate-s-7heresdk8GeoPlaceV5getIDSSyF" class="token"><code>getID()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Allow the client to access GeoPlace id.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getID() -> String
  ```

  </div>

  </div>

  <div>

  #### Return Value

  The place id.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8GeoPlaceV04isMyC0SbyF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-isMyPlace" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geoplace#sdk-for-ios-navigate-s-7heresdk8GeoPlaceV04isMyC0SbyF" class="token"><code>isMyPlace()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Allow the client to access info about is it my place or not.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func isMyPlace() -> Bool
  ```

  </div>

  </div>

  <div>

  #### Return Value

  `True` if it is my place, `false` otherwise.

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

