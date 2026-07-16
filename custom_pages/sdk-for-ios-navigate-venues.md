---
title: "Venues  Reference"
slug: "sdk-for-ios-navigate-venues"
---

# Venues

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9CrosswalkC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-Crosswalk" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk9CrosswalkC" class="token"><code>Crosswalk</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents crosswalk’s inside the <a href="sdk-for-ios-navigate-classes-venuelevel">`VenueLevel`</a>. A crosswalk is an area of the road surface where pedestrians are expected to walk across the road. The area is represented as a polygon, which is often, but not necessarily, rectangular and oriented with the shorter dimension in the vehicle’s direction of travel.

  <a href="sdk-for-ios-navigate-classes-crosswalk" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class Crosswalk
  ```

  ``` highlight
  extension Crosswalk: NativeBase
  ```

  ``` highlight
  extension Crosswalk: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8PropertyC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-Property" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk8PropertyC" class="token"><code>Property</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Holds information of varying types, such as Boolean, Integer, String. Properties are used in <a href="sdk-for-ios-navigate-classes-venuemodel">`VenueModel`</a> <a href="sdk-for-ios-navigate-classes-venuedrawing">`VenueDrawing`</a>, <a href="sdk-for-ios-navigate-classes-venuelevel">`VenueLevel`</a> and <a href="sdk-for-ios-navigate-classes-venuegeometry">`VenueGeometry`</a> to describe this objects.

  <a href="sdk-for-ios-navigate-classes-property" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class Property
  ```

  ``` highlight
  extension Property: NativeBase
  ```

  ``` highlight
  extension Property: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk5VenueC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-Venue" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk5VenueC" class="token"><code>Venue</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Controls the <a href="sdk-for-ios-navigate-classes-venuemodel">`VenueModel`</a> inside the <a href="sdk-for-ios-navigate-classes-venuemap">`VenueMap`</a> object. The venue controls the selection of the <a href="sdk-for-ios-navigate-classes-venuedrawing">`VenueDrawing`</a> and the <a href="sdk-for-ios-navigate-classes-venuelevel">`VenueLevel`</a> of the <a href="sdk-for-ios-navigate-classes-venuemodel">`VenueModel`</a>. It provides the possibility to customize styles for the <a href="sdk-for-ios-navigate-classes-venuegeometry">`VenueGeometry`</a>. Objects of this class can only be created using methods

      VenueMap.addVenueAsync(String, VenueLoadErrorHandler)

  and
      VenueMap.selectVenueAsync(String, VenueLoadErrorHandler)

  .
  </p>

  <a href="sdk-for-ios-navigate-classes-venue" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class Venue
  ```

  ``` highlight
  extension Venue: NativeBase
  ```

  ``` highlight
  extension Venue: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13VenueDelegateP"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Protocol-VenueDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk13VenueDelegateP" class="token"><code>VenueDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The protocol for delegates for venue loading events in <a href="sdk-for-ios-navigate-classes-venueservice">`VenueService`</a>.

  <a href="sdk-for-ios-navigate-protocols-venuedelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol VenueDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12VenueDrawingC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-VenueDrawing" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk12VenueDrawingC" class="token"><code>VenueDrawing</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a drawing inside the <a href="sdk-for-ios-navigate-classes-venuemodel">`VenueModel`</a>. The drawing can be a separate building in a complex of buildings, or show a different view of a venue. For example, in an airport, one drawing can be used as an overview of all buildings in this venue, while other drawings contains details for each terminal in this airport.

  <a href="sdk-for-ios-navigate-classes-venuedrawing" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class VenueDrawing
  ```

  ``` highlight
  extension VenueDrawing: NativeBase
  ```

  ``` highlight
  extension VenueDrawing: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk29VenueDrawingSelectionDelegateP"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Protocol-VenueDrawingSelectionDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk29VenueDrawingSelectionDelegateP" class="token"><code>VenueDrawingSelectionDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The protocol for delegates for the <a href="sdk-for-ios-navigate-classes-venuedrawing">`VenueDrawing`</a> selection event. Use the <a href="sdk-for-ios-navigate-classes-venuemap">`VenueMap`</a> to add and remove the `VenueDrawingSelectionDelegate`.

  <a href="sdk-for-ios-navigate-protocols-venuedrawingselectiondelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol VenueDrawingSelectionDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11VenueEngineC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-VenueEngine" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk11VenueEngineC" class="token"><code>VenueEngine</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  VenueEngine is an add-on to the base map functionality with its own content loading and cache. VenueEngine gives access to the venue functionality, which allows you to load and visualize venues on the map, search content inside venues etc.

  <a href="sdk-for-ios-navigate-classes-venueengine" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class VenueEngine
  ```

  ``` highlight
  extension VenueEngine: NativeBase
  ```

  ``` highlight
  extension VenueEngine: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk32VenueEngineInitCompletionHandlera"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-VenueEngineInitCompletionHandler" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk32VenueEngineInitCompletionHandlera" class="token"><code>VenueEngineInitCompletionHandler</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This method will be called on the main thread when VenueEngine initialization is completed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias VenueEngineInitCompletionHandler = () -> Void
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10VenueErrora"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-VenueError" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk10VenueErrora" class="token"><code>VenueError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies possible errors that may occur during loading of indoor maps

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias VenueError = VenueErrorCode
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-venueerrorcode">VenueErrorCode</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Enum-VenueErrorCode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk14VenueErrorCodeO" class="token"><code>VenueErrorCode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies possible errors that may occur during loading of indoor maps

  <a href="sdk-for-ios-navigate-enums-venueerrorcode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum VenueErrorCode : UInt32, CaseIterable, Codable
  ```

  ``` highlight
  extension VenueErrorCode : Error
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13VenueGeometryC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-VenueGeometry" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk13VenueGeometryC" class="token"><code>VenueGeometry</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a geometry inside the <a href="sdk-for-ios-navigate-classes-venuelevel">`VenueLevel`</a>. The geometry can be any object inside the level, like a room, a wall or a table. Also the geometry can represent virtual objects, like a team area in an open space.

  <a href="sdk-for-ios-navigate-classes-venuegeometry" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class VenueGeometry
  ```

  ``` highlight
  extension VenueGeometry: NativeBase
  ```

  ``` highlight
  extension VenueGeometry: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk23VenueGeometryFilterTypeO"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Enum-VenueGeometryFilterType" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk23VenueGeometryFilterTypeO" class="token"><code>VenueGeometryFilterType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Filter types for the <a href="sdk-for-ios-navigate-classes-venuegeometry">`VenueGeometry`</a> search.

  <a href="sdk-for-ios-navigate-enums-venuegeometryfiltertype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum VenueGeometryFilterType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18VenueGeometryStyleC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-VenueGeometryStyle" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk18VenueGeometryStyleC" class="token"><code>VenueGeometryStyle</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a style of the <a href="sdk-for-ios-navigate-classes-venuegeometry">`VenueGeometry`</a>.

  <a href="sdk-for-ios-navigate-classes-venuegeometrystyle" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class VenueGeometryStyle
  ```

  ``` highlight
  extension VenueGeometryStyle: NativeBase
  ```

  ``` highlight
  extension VenueGeometryStyle: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9VenueInfoC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-VenueInfo" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk9VenueInfoC" class="token"><code>VenueInfo</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the venue info existing in a catalogs contains id and name.

  <a href="sdk-for-ios-navigate-classes-venueinfo" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class VenueInfo
  ```

  ``` highlight
  extension VenueInfo: NativeBase
  ```

  ``` highlight
  extension VenueInfo: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk17VenueInfoDataLista"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-VenueInfoDataList" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk17VenueInfoDataLista" class="token"><code>VenueInfoDataList</code></a> 

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
  public typealias VenueInfoDataList = [VenueInfo]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-venueinfo">VenueInfo</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk29VenueInfoListListenerDelegateP"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Protocol-VenueInfoListListenerDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk29VenueInfoListListenerDelegateP" class="token"><code>VenueInfoListListenerDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The protocol for delegates for the list of <a href="sdk-for-ios-navigate-classes-venueinfo">`VenueInfo`</a> load event. Use <a href="sdk-for-ios-navigate-classes-venuemap">`VenueMap`</a> to add and remove the `VenueInfoListListenerDelegate`.

  <a href="sdk-for-ios-navigate-protocols-venueinfolistlistenerdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol VenueInfoListListenerDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15VenueLabelStyleC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-VenueLabelStyle" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk15VenueLabelStyleC" class="token"><code>VenueLabelStyle</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a style of the label.

  <a href="sdk-for-ios-navigate-classes-venuelabelstyle" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class VenueLabelStyle
  ```

  ``` highlight
  extension VenueLabelStyle: NativeBase
  ```

  ``` highlight
  extension VenueLabelStyle: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10VenueLevelC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-VenueLevel" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk10VenueLevelC" class="token"><code>VenueLevel</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents one level of a building or a complex of buildings inside the <a href="sdk-for-ios-navigate-classes-venuedrawing">`VenueDrawing`</a>.

  <a href="sdk-for-ios-navigate-classes-venuelevel" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class VenueLevel
  ```

  ``` highlight
  extension VenueLevel: NativeBase
  ```

  ``` highlight
  extension VenueLevel: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk27VenueLevelSelectionDelegateP"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Protocol-VenueLevelSelectionDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk27VenueLevelSelectionDelegateP" class="token"><code>VenueLevelSelectionDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The protocol for delegates for the <a href="sdk-for-ios-navigate-classes-venuelevel">`VenueLevel`</a> selection event. Use the <a href="sdk-for-ios-navigate-classes-venuemap">`VenueMap`</a> to add and remove the `VenueLevelSelectionDelegate`.

  <a href="sdk-for-ios-navigate-protocols-venuelevelselectiondelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol VenueLevelSelectionDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22VenueLifecycleDelegateP"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Protocol-VenueLifecycleDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk22VenueLifecycleDelegateP" class="token"><code>VenueLifecycleDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The protocol for delegates for the <a href="sdk-for-ios-navigate-classes-venue">`Venue`</a> lifecycle events. Use the <a href="sdk-for-ios-navigate-classes-venuemap">`VenueMap`</a> to add and remove the `VenueLifecycleDelegate`.

  <a href="sdk-for-ios-navigate-protocols-venuelifecycledelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol VenueLifecycleDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk21VenueLoadErrorHandlera"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-VenueLoadErrorHandler" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk21VenueLoadErrorHandlera" class="token"><code>VenueLoadErrorHandler</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A method which is called on the main thread when

      VenueMap.selectVenueAsync(String, VenueLoadErrorHandler)

  has been completed.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias VenueLoadErrorHandler = (_ error: VenueErrorCode?) -> Void
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-venueerrorcode">VenueErrorCode</a>

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
  <td><code> </code><em><code>error</code></em><code> </code></td>
  <td><div>
  <p>Represents an error in case of a failure. It is <code>nil</code> for an operation that succeeds.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8VenueMapC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-VenueMap" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk8VenueMapC" class="token"><code>VenueMap</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Connects a map with venues. When the `VenueMap` is started, venues can be seen on the map as interactive models. The user can switch drawings and levels, change a visual style of geometries and related labels inside the venue etc. After constructing the `VenueMap`, delegates for relevant events should be added to the object. `VenueMap` is an add-on to the base map functionality with its own content loading and cache. For this reason, in certain situations there may be a small delay before the venue is visible.

  <a href="sdk-for-ios-navigate-classes-venuemap" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

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

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16VenueMapDelegateP"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Protocol-VenueMapDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk16VenueMapDelegateP" class="token"><code>VenueMapDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The protocol for delegates for venue loading events in <a href="sdk-for-ios-navigate-classes-venueservice">`VenueService`</a>.

  <a href="sdk-for-ios-navigate-protocols-venuemapdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol VenueMapDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25VenueMapLifecycleDelegateP"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Protocol-VenueMapLifecycleDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk25VenueMapLifecycleDelegateP" class="token"><code>VenueMapLifecycleDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The protocol for delegates for the <a href="sdk-for-ios-navigate-classes-venue">`Venue`</a> lifecycle events. Use the <a href="sdk-for-ios-navigate-classes-venuemap">`VenueMap`</a> to add and remove the `VenueMapLifecycleDelegate`.

  <a href="sdk-for-ios-navigate-protocols-venuemaplifecycledelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol VenueMapLifecycleDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10VenueModelC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-VenueModel" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk10VenueModelC" class="token"><code>VenueModel</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a building or a complex of buildings, like airports or universities.

  <a href="sdk-for-ios-navigate-classes-venuemodel" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class VenueModel
  ```

  ``` highlight
  extension VenueModel: NativeBase
  ```

  ``` highlight
  extension VenueModel: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22VenueSelectionDelegateP"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Protocol-VenueSelectionDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk22VenueSelectionDelegateP" class="token"><code>VenueSelectionDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The protocol for delegates for the <a href="sdk-for-ios-navigate-classes-venue">`Venue`</a> selection event. Use the <a href="sdk-for-ios-navigate-classes-venuemap">`VenueMap`</a> to add and remove the `VenueSelectionDelegate`.

  <a href="sdk-for-ios-navigate-protocols-venueselectiondelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol VenueSelectionDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12VenueServiceC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-VenueService" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk12VenueServiceC" class="token"><code>VenueService</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Offers methods to download venues. Use of this object does not necessitate Map involvement.

  Before loading the venues, initialize the venue service with one of the start methods.

  The venue service is online only. Even if there is a cached venue on the device, the venue service requires an online connection to check if the venue is available for the user.

  <a href="sdk-for-ios-navigate-classes-venueservice" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class VenueService
  ```

  ``` highlight
  extension VenueService: NativeBase
  ```

  ``` highlight
  extension VenueService: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20VenueServiceDelegateP"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Protocol-VenueServiceDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk20VenueServiceDelegateP" class="token"><code>VenueServiceDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The protocol for delegates for lifecycle events in <a href="sdk-for-ios-navigate-classes-venueservice">`VenueService`</a>.

  <a href="sdk-for-ios-navigate-protocols-venueservicedelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol VenueServiceDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22VenueServiceInitStatusO"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Enum-VenueServiceInitStatus" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk22VenueServiceInitStatusO" class="token"><code>VenueServiceInitStatus</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Initialization status types of the <a href="sdk-for-ios-navigate-classes-venueservice">`VenueService`</a>.

  <a href="sdk-for-ios-navigate-enums-venueserviceinitstatus" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum VenueServiceInitStatus : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10VenueStyleC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-VenueStyle" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk10VenueStyleC" class="token"><code>VenueStyle</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a style of the venue. Contains the information about the geometry and label styles available for the venue.

  <a href="sdk-for-ios-navigate-classes-venuestyle" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class VenueStyle
  ```

  ``` highlight
  extension VenueStyle: NativeBase
  ```

  ``` highlight
  extension VenueStyle: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13VenueTopologyC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-VenueTopology" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk13VenueTopologyC" class="token"><code>VenueTopology</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents routing topologies inside the <a href="sdk-for-ios-navigate-classes-venuelevel">`VenueLevel`</a>. The topologies can be paths used for enabling routing services.

  <a href="sdk-for-ios-navigate-classes-venuetopology" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class VenueTopology
  ```

  ``` highlight
  extension VenueTopology: NativeBase
  ```

  ``` highlight
  extension VenueTopology: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18VenueTransportModeO"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Enum-VenueTransportMode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-venues#sdk-for-ios-navigate-s-7heresdk18VenueTransportModeO" class="token"><code>VenueTransportMode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Available mode of transport on indoor topology.

  <a href="sdk-for-ios-navigate-enums-venuetransportmode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum VenueTransportMode : UInt32, CaseIterable, Codable
  ```

  </div>

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

