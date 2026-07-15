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

  ` `<span id="/s:7heresdk8VenueMapC0B8InfoLista"></span>` `<span id="//apple_ref/swift/Alias/VenueInfoList" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-venuemap#/s:7heresdk8VenueMapC0B8InfoLista" class="token"><code>VenueInfoList</code></a>` `

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

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8VenueMapC12venueServiceAA0bE0Cvp"></span>` `<span id="//apple_ref/swift/Property/venueService" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-venuemap#/s:7heresdk8VenueMapC12venueServiceAA0bE0Cvp" class="token"><code>venueService</code></a>` `

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

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8VenueMapC08selectedB0AA0B0CSgvp"></span>` `<span id="//apple_ref/swift/Property/selectedVenue" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-venuemap#/s:7heresdk8VenueMapC08selectedB0AA0B0CSgvp" class="token"><code>selectedVenue</code></a>` `

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

  </div>

  </div>

  </div>

- <div>

      addVenueAsync(venueId: )

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
  public func addVenueAsync ( venueId : Int32 )
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

      addVenueAsync(venueIdentifier: )

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
  public func addVenueAsync ( venueIdentifier : String )
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

      addVenueAsync(venueId: completion: )

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
  public func addVenueAsync ( venueId : Int32 , completion : @escaping VenueLoadErrorHandler )
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

      addVenueAsync(venueIdentifier: completion: )

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
  public func addVenueAsync ( venueIdentifier : String , completion : @escaping VenueLoadErrorHandler )
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

      removeVenue(venue: )

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
  public func removeVenue ( venue : Venue )
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

      selectVenueAsync(venueId: )

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
  public func selectVenueAsync ( venueId : Int32 )
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

      selectVenueAsync(venueIdentifier: )

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
  public func selectVenueAsync ( venueIdentifier : String )
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

      selectVenueAsync(venueId: completion: )

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
  public func selectVenueAsync ( venueId : Int32 , completion : @escaping VenueLoadErrorHandler )
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

      selectVenueAsync(venueIdentifier: completion: )

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
  public func selectVenueAsync ( venueIdentifier : String , completion : @escaping VenueLoadErrorHandler )
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

      cancelVenueSelection()

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
  public func cancelVenueSelection () -> Bool
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  `True` if a venue was about to load and `false` otherwise.

  </div>

  </div>

  </div>

- <div>

      getVenue(position: )

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
  public func getVenue ( position : GeoCoordinates ) -> Venue ?
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

      getGeometry(position: )

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
  public func getGeometry ( position : GeoCoordinates ) -> VenueGeometry ?
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

      addVenueLifecycleDelegate(_: )

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
  public func addVenueLifecycleDelegate ( _ delegate : VenueLifecycleDelegate )
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

      removeVenueLifecycleDelegate(_: )

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
  public func removeVenueLifecycleDelegate ( _ delegate : VenueLifecycleDelegate )
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

      addVenueMapLifecycleDelegate(_: )

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
  public func addVenueMapLifecycleDelegate ( _ delegate : VenueMapLifecycleDelegate )
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

      removeVenueMapLifecycleDelegate(_: )

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
  public func removeVenueMapLifecycleDelegate ( _ delegate : VenueMapLifecycleDelegate )
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

      addVenueSelectionDelegate(_: )

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
  public func addVenueSelectionDelegate ( _ delegate : VenueSelectionDelegate )
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

      removeVenueSelectionDelegate(_: )

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
  public func removeVenueSelectionDelegate ( _ delegate : VenueSelectionDelegate )
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

      addDrawingSelectionDelegate(_: )

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
  public func addDrawingSelectionDelegate ( _ delegate : VenueDrawingSelectionDelegate )
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

      removeDrawingSelectionDelegate(_: )

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
  public func removeDrawingSelectionDelegate ( _ delegate : VenueDrawingSelectionDelegate )
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

      addLevelSelectionDelegate(_: )

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
  public func addLevelSelectionDelegate ( _ delegate : VenueLevelSelectionDelegate )
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

      removeLevelSelectionDelegate(_: )

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
  public func removeLevelSelectionDelegate ( _ delegate : VenueLevelSelectionDelegate )
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

      addVenueInfoListDelegate(_: )

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
  public func addVenueInfoListDelegate ( _ delegate : VenueInfoListListenerDelegate )
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

      removeVenueInfoListDelegate(_: )

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
  public func removeVenueInfoListDelegate ( _ delegate : VenueInfoListListenerDelegate )
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

      getVenueInfoList()

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
  public func getVenueInfoList () -> VenueMap . VenueInfoList
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  returns the list of object of <a href="sdk-for-ios-explore-classes-venueinfo">`VenueInfo`</a>.

  </div>

  </div>

  </div>

- <div>

      getVenueInfoList(completion: )

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
  public func getVenueInfoList ( completion : @escaping VenueLoadErrorHandler ) -> VenueMap . VenueInfoList
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

      getVenueInfoListAsync()

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
  public func getVenueInfoListAsync ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      getVenueInfoListAsync(completion: )

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
  public func getVenueInfoListAsync ( completion : @escaping VenueLoadErrorHandler )
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

      getTopology(position: )

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
  public func getTopology ( position : GeoCoordinates ) -> VenueTopology ?
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

      getCrosswalk(position: )

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
  public func getCrosswalk ( position : GeoCoordinates ) -> Crosswalk ?
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

