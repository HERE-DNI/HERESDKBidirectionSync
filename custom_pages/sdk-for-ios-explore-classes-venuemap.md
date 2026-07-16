---
title: "VenueMap Class Reference"
slug: "sdk-for-ios-explore-classes-venuemap"
---

# VenueMap

<div class="declaration">

<div class="language">

``` highlight
public class VenueMap
```

``` highlight
extension VenueMap: NativeBase
```

``` highlight
extension VenueMap: Hashable
```

</div>

</div>

Connects a map with venues. When the `VenueMap` is started, venues can be seen on the map as interactive models. The user can switch drawings and levels, change a visual style of geometries and related labels inside the venue etc. After constructing the `VenueMap`, delegates for relevant events should be added to the object. `VenueMap` is an add-on to the base map functionality with its own content loading and cache. For this reason, in certain situations there may be a small delay before the venue is visible.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC0B8InfoLista"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Alias-VenueInfoList" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC0B8InfoLista" class="token"><code>VenueInfoList</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Undocumented

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias VenueInfoList = [VenueInfo]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-venueinfo">VenueInfo</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC12venueServiceAA0bE0Cvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-venueService" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC12venueServiceAA0bE0Cvp" class="token"><code>venueService</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The <a href="sdk-for-ios-explore-classes-venueservice">`VenueService`</a> object. It can be used to search and get the <a href="sdk-for-ios-explore-classes-venuemodel">`VenueModel`</a> objects.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var venueService: VenueService { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-venueservice">VenueService</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC08selectedB0AA0B0CSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-selectedVenue" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC08selectedB0AA0B0CSgvp" class="token"><code>selectedVenue</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The selected venue or `nil` if no venue is selected. Use `nil` to deselect the venue.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var selectedVenue: Venue? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-venue">Venue</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC03addB5Async7venueIdys5Int32V_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addVenueAsync-venueId" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC03addB5Async7venueIdys5Int32V_tF" class="token"><code>addVenueAsync(venueId:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Downloads and adds a <a href="sdk-for-ios-explore-classes-venue">`Venue`</a> to the `VenueMap`. Method will do nothing if the venue already exists on the venue map.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addVenueAsync(venueId: Int32)
  ```

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
  <td><code> </code><em><code>venueId</code></em><code> </code></td>
  <td><div>
  <p>The ID of the venue to download and add.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC03addB5Async15venueIdentifierySS_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addVenueAsync-venueIdentifier" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC03addB5Async15venueIdentifierySS_tF" class="token"><code>addVenueAsync(venueIdentifier:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Downloads and adds a <a href="sdk-for-ios-explore-classes-venue">`Venue`</a> to the `VenueMap`. Method will do nothing if the venue already exists on the venue map.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addVenueAsync(venueIdentifier: String)
  ```

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
  <td><code> </code><em><code>venueIdentifier</code></em><code> </code></td>
  <td><div>
  <p>The ID of the venue to download and add.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC03addB5Async7venueId10completionys5Int32V_yAA0B9ErrorCodeOSgctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addVenueAsync-venueId-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC03addB5Async7venueId10completionys5Int32V_yAA0B9ErrorCodeOSgctF" class="token"><code>addVenueAsync(venueId:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Downloads and adds a <a href="sdk-for-ios-explore-classes-venue">`Venue`</a> to the `VenueMap`. Method will do nothing if the venue already exists on the venue map.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addVenueAsync(venueId: Int32, completion: @escaping VenueLoadErrorHandler)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-venues#sdk-for-ios-explore-s-7heresdk21VenueLoadErrorHandlera">VenueLoadErrorHandler</a>

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
  <td><code> </code><em><code>venueId</code></em><code> </code></td>
  <td><div>
  <p>The ID of the venue to download and add.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback to receives the error while venue load on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC03addB5Async15venueIdentifier10completionySS_yAA0B9ErrorCodeOSgctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addVenueAsync-venueIdentifier-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC03addB5Async15venueIdentifier10completionySS_yAA0B9ErrorCodeOSgctF" class="token"><code>addVenueAsync(venueIdentifier:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Downloads and adds a <a href="sdk-for-ios-explore-classes-venue">`Venue`</a> to the `VenueMap`. Method will do nothing if the venue already exists on the venue map.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addVenueAsync(venueIdentifier: String, completion: @escaping VenueLoadErrorHandler)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-venues#sdk-for-ios-explore-s-7heresdk21VenueLoadErrorHandlera">VenueLoadErrorHandler</a>

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
  <td><code> </code><em><code>venueIdentifier</code></em><code> </code></td>
  <td><div>
  <p>The ID of the venue to download and add.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback to receives the error while venue load on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC06removeB05venueyAA0B0C_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeVenue-venue" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC06removeB05venueyAA0B0C_tF" class="token"><code>removeVenue(venue:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a <a href="sdk-for-ios-explore-classes-venue">`Venue`</a> from the `VenueMap`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeVenue(venue: Venue)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-venue">Venue</a>

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
  <td><code> </code><em><code>venue</code></em><code> </code></td>
  <td><div>
  <p>The venue to remove.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC06selectB5Async7venueIdys5Int32V_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-selectVenueAsync-venueId" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC06selectB5Async7venueIdys5Int32V_tF" class="token"><code>selectVenueAsync(venueId:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Downloads a <a href="sdk-for-ios-explore-classes-venuemodel">`VenueModel`</a> if needed and selects a <a href="sdk-for-ios-explore-classes-venue">`Venue`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func selectVenueAsync(venueId: Int32)
  ```

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
  <td><code> </code><em><code>venueId</code></em><code> </code></td>
  <td><div>
  <p>The ID of the venue to download and select.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC06selectB5Async15venueIdentifierySS_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-selectVenueAsync-venueIdentifier" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC06selectB5Async15venueIdentifierySS_tF" class="token"><code>selectVenueAsync(venueIdentifier:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Downloads a <a href="sdk-for-ios-explore-classes-venuemodel">`VenueModel`</a> if needed and selects a <a href="sdk-for-ios-explore-classes-venue">`Venue`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func selectVenueAsync(venueIdentifier: String)
  ```

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
  <td><code> </code><em><code>venueIdentifier</code></em><code> </code></td>
  <td><div>
  <p>The ID of the venue to download and select.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC06selectB5Async7venueId10completionys5Int32V_yAA0B9ErrorCodeOSgctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-selectVenueAsync-venueId-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC06selectB5Async7venueId10completionys5Int32V_yAA0B9ErrorCodeOSgctF" class="token"><code>selectVenueAsync(venueId:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Downloads a <a href="sdk-for-ios-explore-classes-venuemodel">`VenueModel`</a> if needed and selects a <a href="sdk-for-ios-explore-classes-venue">`Venue`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func selectVenueAsync(venueId: Int32, completion: @escaping VenueLoadErrorHandler)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-venues#sdk-for-ios-explore-s-7heresdk21VenueLoadErrorHandlera">VenueLoadErrorHandler</a>

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
  <td><code> </code><em><code>venueId</code></em><code> </code></td>
  <td><div>
  <p>The ID of the venue to download and select.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback to receives the error while venue load on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC06selectB5Async15venueIdentifier10completionySS_yAA0B9ErrorCodeOSgctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-selectVenueAsync-venueIdentifier-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC06selectB5Async15venueIdentifier10completionySS_yAA0B9ErrorCodeOSgctF" class="token"><code>selectVenueAsync(venueIdentifier:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Downloads a <a href="sdk-for-ios-explore-classes-venuemodel">`VenueModel`</a> if needed and selects a <a href="sdk-for-ios-explore-classes-venue">`Venue`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func selectVenueAsync(venueIdentifier: String, completion: @escaping VenueLoadErrorHandler)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-venues#sdk-for-ios-explore-s-7heresdk21VenueLoadErrorHandlera">VenueLoadErrorHandler</a>

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
  <td><code> </code><em><code>venueIdentifier</code></em><code> </code></td>
  <td><div>
  <p>The ID of the venue to download and select.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback to receives the error while venue load on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC06cancelB9SelectionSbyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-cancelVenueSelection" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC06cancelB9SelectionSbyF" class="token"><code>cancelVenueSelection()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Attempts to cancel venue loading and selection that may currently be in progress.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func cancelVenueSelection() -> Bool
  ```

  </div>

  </div>

  <div>

  #### Return Value

  `True` if a venue was about to load and `false` otherwise.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC03getB08positionAA0B0CSgAA14GeoCoordinatesV_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getVenue-position" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC03getB08positionAA0B0CSgAA14GeoCoordinatesV_tF" class="token"><code>getVenue(position:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Tries to find a <a href="sdk-for-ios-explore-classes-venue">`Venue`</a> at the specified geographic coordinates.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getVenue(position: GeoCoordinates) -> Venue?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>
  - <a href="sdk-for-ios-explore-classes-venue">Venue</a>

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
  <td><code> </code><em><code>position</code></em><code> </code></td>
  <td><div>
  <p>Geographic coordinates where a venue is located.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Venue or `nil` if there is no venue at the specified geographic coordinates.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC11getGeometry8positionAA0bE0CSgAA14GeoCoordinatesV_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getGeometry-position" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC11getGeometry8positionAA0bE0CSgAA14GeoCoordinatesV_tF" class="token"><code>getGeometry(position:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Tries to find a <a href="sdk-for-ios-explore-classes-venuegeometry">`VenueGeometry`</a> at the specified geographic coordinates in the selected <a href="sdk-for-ios-explore-classes-venue">`Venue`</a> in the currently selected <a href="sdk-for-ios-explore-classes-venuelevel">`VenueLevel`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getGeometry(position: GeoCoordinates) -> VenueGeometry?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>
  - <a href="sdk-for-ios-explore-classes-venuegeometry">VenueGeometry</a>

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
  <td><code> </code><em><code>position</code></em><code> </code></td>
  <td><div>
  <p>Geographic coordinates where the geometry is located.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Geometry or `nil` if there is no geometry at the specified geographic coordinates.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC03addB17LifecycleDelegateyyAA0beF0_pF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addVenueLifecycleDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC03addB17LifecycleDelegateyyAA0beF0_pF" class="token"><code>addVenueLifecycleDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a venue lifecycle delegate.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addVenueLifecycleDelegate(_ delegate: VenueLifecycleDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-venuelifecycledelegate">VenueLifecycleDelegate</a>

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
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The delegate to add.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC06removeB17LifecycleDelegateyyAA0beF0_pF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeVenueLifecycleDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC06removeB17LifecycleDelegateyyAA0beF0_pF" class="token"><code>removeVenueLifecycleDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a venue lifecycle delegate.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeVenueLifecycleDelegate(_ delegate: VenueLifecycleDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-venuelifecycledelegate">VenueLifecycleDelegate</a>

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
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The delegate to remove.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC03addbC17LifecycleDelegateyyAA0bceF0_pF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addVenueMapLifecycleDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC03addbC17LifecycleDelegateyyAA0bceF0_pF" class="token"><code>addVenueMapLifecycleDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a venue map lifecycle delegate.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addVenueMapLifecycleDelegate(_ delegate: VenueMapLifecycleDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-venuemaplifecycledelegate">VenueMapLifecycleDelegate</a>

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
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The delegate to add.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC06removebC17LifecycleDelegateyyAA0bceF0_pF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeVenueMapLifecycleDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC06removebC17LifecycleDelegateyyAA0bceF0_pF" class="token"><code>removeVenueMapLifecycleDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a venue map lifecycle delegate.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeVenueMapLifecycleDelegate(_ delegate: VenueMapLifecycleDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-venuemaplifecycledelegate">VenueMapLifecycleDelegate</a>

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
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The delegate to remove.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC03addB17SelectionDelegateyyAA0beF0_pF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addVenueSelectionDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC03addB17SelectionDelegateyyAA0beF0_pF" class="token"><code>addVenueSelectionDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a venue selection delegate.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addVenueSelectionDelegate(_ delegate: VenueSelectionDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-venueselectiondelegate">VenueSelectionDelegate</a>

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
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The delegate to add.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC06removeB17SelectionDelegateyyAA0beF0_pF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeVenueSelectionDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC06removeB17SelectionDelegateyyAA0beF0_pF" class="token"><code>removeVenueSelectionDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a venue selection delegate.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeVenueSelectionDelegate(_ delegate: VenueSelectionDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-venueselectiondelegate">VenueSelectionDelegate</a>

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
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The delegate to remove.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC27addDrawingSelectionDelegateyyAA0befG0_pF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addDrawingSelectionDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC27addDrawingSelectionDelegateyyAA0befG0_pF" class="token"><code>addDrawingSelectionDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a drawing selection delegate.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addDrawingSelectionDelegate(_ delegate: VenueDrawingSelectionDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-venuedrawingselectiondelegate">VenueDrawingSelectionDelegate</a>

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
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The delegate to add.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC30removeDrawingSelectionDelegateyyAA0befG0_pF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeDrawingSelectionDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC30removeDrawingSelectionDelegateyyAA0befG0_pF" class="token"><code>removeDrawingSelectionDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a drawing selection delegate.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeDrawingSelectionDelegate(_ delegate: VenueDrawingSelectionDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-venuedrawingselectiondelegate">VenueDrawingSelectionDelegate</a>

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
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The delegate to remove.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC25addLevelSelectionDelegateyyAA0befG0_pF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addLevelSelectionDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC25addLevelSelectionDelegateyyAA0befG0_pF" class="token"><code>addLevelSelectionDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a level selection delegate.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addLevelSelectionDelegate(_ delegate: VenueLevelSelectionDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-venuelevelselectiondelegate">VenueLevelSelectionDelegate</a>

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
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The delegate to add.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC28removeLevelSelectionDelegateyyAA0befG0_pF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeLevelSelectionDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC28removeLevelSelectionDelegateyyAA0befG0_pF" class="token"><code>removeLevelSelectionDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a level selection delegate.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeLevelSelectionDelegate(_ delegate: VenueLevelSelectionDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-venuelevelselectiondelegate">VenueLevelSelectionDelegate</a>

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
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The delegate to remove.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC03addB16InfoListDelegateyyAA0bef8ListenerG0_pF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addVenueInfoListDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC03addB16InfoListDelegateyyAA0bef8ListenerG0_pF" class="token"><code>addVenueInfoListDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a listener to handle the completion of the asynchronous venue info list retrieval.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addVenueInfoListDelegate(_ delegate: VenueInfoListListenerDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-venueinfolistlistenerdelegate">VenueInfoListListenerDelegate</a>

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
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The listener to add.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC06removeB16InfoListDelegateyyAA0bef8ListenerG0_pF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeVenueInfoListDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC06removeB16InfoListDelegateyyAA0bef8ListenerG0_pF" class="token"><code>removeVenueInfoListDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a listener for the asynchronous venue info list retrieval.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeVenueInfoListDelegate(_ delegate: VenueInfoListListenerDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-venueinfolistlistenerdelegate">VenueInfoListListenerDelegate</a>

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
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The listener to remove.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC03getB8InfoListSayAA0bE0CGyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getVenueInfoList" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC03getB8InfoListSayAA0bE0CGyF" class="token"><code>getVenueInfoList()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of <a href="sdk-for-ios-explore-classes-venueinfo">`VenueInfo`</a> contains venue id and name.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getVenueInfoList() -> VenueMap.VenueInfoList
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC0B8InfoLista">VenueInfoList</a>

  </div>

  <div>

  #### Return Value

  returns the list of object of <a href="sdk-for-ios-explore-classes-venueinfo">`VenueInfo`</a>.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC03getB8InfoList10completionSayAA0bE0CGyAA0B9ErrorCodeOSgc_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getVenueInfoList-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC03getB8InfoList10completionSayAA0bE0CGyAA0B9ErrorCodeOSgc_tF" class="token"><code>getVenueInfoList(completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of <a href="sdk-for-ios-explore-classes-venueinfo">`VenueInfo`</a> contains venue id and name.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getVenueInfoList(completion: @escaping VenueLoadErrorHandler) -> VenueMap.VenueInfoList
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-venues#sdk-for-ios-explore-s-7heresdk21VenueLoadErrorHandlera">VenueLoadErrorHandler</a>
  - <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC0B8InfoLista">VenueInfoList</a>

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
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback to receives the error while venue load on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  returns the list of object of <a href="sdk-for-ios-explore-classes-venueinfo">`VenueInfo`</a>.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC03getB13InfoListAsyncyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getVenueInfoListAsync" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC03getB13InfoListAsyncyyF" class="token"><code>getVenueInfoListAsync()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of <a href="sdk-for-ios-explore-classes-venueinfo">`VenueInfo`</a> contains venue id and name. Downloads the list of <a href="sdk-for-ios-explore-classes-venueinfo">`VenueInfo`</a> asynchronously.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getVenueInfoListAsync()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC03getB13InfoListAsync10completionyyAA0B9ErrorCodeOSgc_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getVenueInfoListAsync-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC03getB13InfoListAsync10completionyyAA0B9ErrorCodeOSgc_tF" class="token"><code>getVenueInfoListAsync(completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of <a href="sdk-for-ios-explore-classes-venueinfo">`VenueInfo`</a> contains venue id and name. Downloads the list of <a href="sdk-for-ios-explore-classes-venueinfo">`VenueInfo`</a> asynchronously.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getVenueInfoListAsync(completion: @escaping VenueLoadErrorHandler)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-venues#sdk-for-ios-explore-s-7heresdk21VenueLoadErrorHandlera">VenueLoadErrorHandler</a>

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
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback to receive the list of venue info if successful.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC11getTopology8positionAA0bE0CSgAA14GeoCoordinatesV_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getTopology-position" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC11getTopology8positionAA0bE0CSgAA14GeoCoordinatesV_tF" class="token"><code>getTopology(position:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Tries to find a <a href="sdk-for-ios-explore-classes-venuetopology">`VenueTopology`</a> at the specified geographic coordinates in the selected <a href="sdk-for-ios-explore-classes-venue">`Venue`</a> in the currently selected <a href="sdk-for-ios-explore-classes-venuelevel">`VenueLevel`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getTopology(position: GeoCoordinates) -> VenueTopology?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>
  - <a href="sdk-for-ios-explore-classes-venuetopology">VenueTopology</a>

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
  <td><code> </code><em><code>position</code></em><code> </code></td>
  <td><div>
  <p>Geographic coordinates where the topology is located.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Topology or `nil` if there is no topology at the specified geographic coordinates.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8VenueMapC12getCrosswalk8positionAA0E0CSgAA14GeoCoordinatesV_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getCrosswalk-position" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuemap#sdk-for-ios-explore-s-7heresdk8VenueMapC12getCrosswalk8positionAA0E0CSgAA14GeoCoordinatesV_tF" class="token"><code>getCrosswalk(position:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Tries to find a <a href="sdk-for-ios-explore-classes-crosswalk">`Crosswalk`</a> at the specified geographic coordinates in the selected <a href="sdk-for-ios-explore-classes-venue">`Venue`</a> in the currently selected <a href="sdk-for-ios-explore-classes-venuelevel">`VenueLevel`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getCrosswalk(position: GeoCoordinates) -> Crosswalk?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>
  - <a href="sdk-for-ios-explore-classes-crosswalk">Crosswalk</a>

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
  <td><code> </code><em><code>position</code></em><code> </code></td>
  <td><div>
  <p>Geographic coordinates where the crosswalk is located.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Crosswalk or `nil` if there is no crosswalk at the specified geographic coordinates.

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

