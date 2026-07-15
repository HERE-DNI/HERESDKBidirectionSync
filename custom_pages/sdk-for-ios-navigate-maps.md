---
title: "Maps  Reference"
slug: "sdk-for-ios-navigate-maps"
---

# Maps

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk17AnimationDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/AnimationDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk17AnimationDelegateP" class="token"><code>AnimationDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A delegate for animation events.

  <a href="sdk-for-ios-navigate-protocols-animationdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol AnimationDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14AnimationStateO"></span>` `<span id="//apple_ref/swift/Enum/AnimationState" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk14AnimationStateO" class="token"><code>AnimationState</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes the possible states of an animation.

  <a href="sdk-for-ios-navigate-enums-animationstate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum AnimationState : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13AssetsManagerC"></span>` `<span id="//apple_ref/swift/Class/AssetsManager" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk13AssetsManagerC" class="token"><code>AssetsManager</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Assets manager interface. Can be used to make assets available to the SDK.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-assetsmanager" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class AssetsManager
  ```

  ``` highlight
  extension AssetsManager: NativeBase
  ```

  ``` highlight
  extension AssetsManager: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14DataAttributesC"></span>` `<span id="//apple_ref/swift/Class/DataAttributes" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk14DataAttributesC" class="token"><code>DataAttributes</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Data attributes collection.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-dataattributes" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class DataAttributes : DataAttributesBase
  ```

  ``` highlight
  extension DataAttributes: NativeBase
  ```

  ``` highlight
  extension DataAttributes: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22DataAttributesAccessorC"></span>` `<span id="//apple_ref/swift/Class/DataAttributesAccessor" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk22DataAttributesAccessorC" class="token"><code>DataAttributesAccessor</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Accessor used for manipulating data attributes.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-dataattributesaccessor" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class DataAttributesAccessor : DataAttributesBase
  ```

  ``` highlight
  extension DataAttributesAccessor: NativeBase
  ```

  ``` highlight
  extension DataAttributesAccessor: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21DataAttributesBuilderC"></span>` `<span id="//apple_ref/swift/Class/DataAttributesBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk21DataAttributesBuilderC" class="token"><code>DataAttributesBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Data attributes collection builder.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-dataattributesbuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class DataAttributesBuilder
  ```

  ``` highlight
  extension DataAttributesBuilder: NativeBase
  ```

  ``` highlight
  extension DataAttributesBuilder: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18DataAttributeValueC"></span>` `<span id="//apple_ref/swift/Class/DataAttributeValue" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk18DataAttributeValueC" class="token"><code>DataAttributeValue</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Encapsulates a data attribute value. Supports basic types and arrays of basic types.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-dataattributevalue" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class DataAttributeValue
  ```

  ``` highlight
  extension DataAttributeValue: NativeBase
  ```

  ``` highlight
  extension DataAttributeValue: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11DashPatternV"></span>` `<span id="//apple_ref/swift/Struct/DashPattern" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk11DashPatternV" class="token"><code>DashPattern</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a dash pattern for map polyline.

  <a href="sdk-for-ios-navigate-structs-dashpattern" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct DashPattern : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17DoubleTapDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/DoubleTapDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk17DoubleTapDelegateP" class="token"><code>DoubleTapDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol for handling double tap gestures. Double-tap gesture occurs after double-tapping on the screen.

  <a href="sdk-for-ios-navigate-protocols-doubletapdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol DoubleTapDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13DrawOrderTypeO"></span>` `<span id="//apple_ref/swift/Enum/DrawOrderType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk13DrawOrderTypeO" class="token"><code>DrawOrderType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the type of map item draw order. Map item rendering behavior is chosen based on the draw order type.

  Regardless of a draw order type map items with a higher draw order are drawn on top of map items with a lower draw order.

  When having map items in a scene with the same draw order, but with different draw order types <a href="sdk-for-ios-navigate-enums-drawordertype#/s:7heresdk13DrawOrderTypeO016mapSceneAdditionC9DependentyA2CmF">`DrawOrderType.mapSceneAdditionOrderDependent`</a> and <a href="sdk-for-ios-navigate-enums-drawordertype#/s:7heresdk13DrawOrderTypeO016mapSceneAdditionC11IndependentyA2CmF">`DrawOrderType.mapSceneAdditionOrderIndependent`</a>, <a href="sdk-for-ios-navigate-enums-drawordertype#/s:7heresdk13DrawOrderTypeO016mapSceneAdditionC9DependentyA2CmF">`DrawOrderType.mapSceneAdditionOrderDependent`</a> items will be rendered on top of <a href="sdk-for-ios-navigate-enums-drawordertype#/s:7heresdk13DrawOrderTypeO016mapSceneAdditionC11IndependentyA2CmF">`DrawOrderType.mapSceneAdditionOrderIndependent`</a> ones.

  <a href="sdk-for-ios-navigate-enums-drawordertype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum DrawOrderType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk6EasingC"></span>` `<span id="//apple_ref/swift/Class/Easing" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk6EasingC" class="token"><code>Easing</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Animation easing representing an easing function to be used during animations.

  <a href="sdk-for-ios-navigate-classes-easing" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class Easing
  ```

  ``` highlight
  extension Easing: NativeBase
  ```

  ``` highlight
  extension Easing: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14EasingFunctionO"></span>` `<span id="//apple_ref/swift/Enum/EasingFunction" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk14EasingFunctionO" class="token"><code>EasingFunction</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Animation easing functions.

  <a href="sdk-for-ios-navigate-enums-easingfunction" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum EasingFunction : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22GeoCoordinatesKeyframeV"></span>` `<span id="//apple_ref/swift/Struct/GeoCoordinatesKeyframe" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk22GeoCoordinatesKeyframeV" class="token"><code>GeoCoordinatesKeyframe</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A GeoCoordinatesKeyframe consists of a GeoCoordinates and an animation duration.

  <a href="sdk-for-ios-navigate-structs-geocoordinateskeyframe" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct GeoCoordinatesKeyframe : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22GeoOrientationKeyframeV"></span>` `<span id="//apple_ref/swift/Struct/GeoOrientationKeyframe" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk22GeoOrientationKeyframeV" class="token"><code>GeoOrientationKeyframe</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A GeoOrientationKeyframe consists of a GeoOrientation (camera orientation) and an animation duration.

  <a href="sdk-for-ios-navigate-structs-geoorientationkeyframe" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct GeoOrientationKeyframe : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12GestureStateO"></span>` `<span id="//apple_ref/swift/Enum/GestureState" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk12GestureStateO" class="token"><code>GestureState</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the state of the gesture.

  <a href="sdk-for-ios-navigate-enums-gesturestate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum GestureState : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11GestureTypeO"></span>` `<span id="//apple_ref/swift/Enum/GestureType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk11GestureTypeO" class="token"><code>GestureType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Enum that represents the type of a gesture.

  <a href="sdk-for-ios-navigate-enums-gesturetype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum GestureType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8GesturesC"></span>` `<span id="//apple_ref/swift/Class/Gestures" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk8GesturesC" class="token"><code>Gestures</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Use this class to process touch events from the platform and detect gesture induced actions on the map view. Please note that this class holds strong references to the gesture delegates.

  <a href="sdk-for-ios-navigate-classes-gestures" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class Gestures
  ```

  ``` highlight
  extension Gestures: NativeBase
  ```

  ``` highlight
  extension Gestures: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7HereMapC"></span>` `<span id="//apple_ref/swift/Class/HereMap" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk7HereMapC" class="token"><code>HereMap</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The representation of a dynamic and interactive geographic map. The map manages a collection of layers of objects and spaces, presents them in a stacked layout and offers the means to focus on a certain area. The layers, their relation to the objects and spaces, the layout and the representation style is described through a configuration.

  <a href="sdk-for-ios-navigate-classes-heremap" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class HereMap
  ```

  ``` highlight
  extension HereMap: NativeBase
  ```

  ``` highlight
  extension HereMap: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12IconProviderC"></span>` `<span id="//apple_ref/swift/Class/IconProvider" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk12IconProviderC" class="token"><code>IconProvider</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This provider creates icons from a given set of parameters for map content and constraints for icon dimensions for a particular map scheme. The icon creation currently does not rely on map data. Therefore, it works without online connection.

  <div class="aside aside-note">

  Note

  This feature is in BETA state and thus there can be bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  <a href="sdk-for-ios-navigate-classes-iconprovider" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class IconProvider
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21IconProviderAssetTypeO"></span>` `<span id="//apple_ref/swift/Enum/IconProviderAssetType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk21IconProviderAssetTypeO" class="token"><code>IconProviderAssetType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asset types for loading icons.

  <a href="sdk-for-ios-navigate-enums-iconproviderassettype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum IconProviderAssetType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20IconProviderCallbacka"></span>` `<span id="//apple_ref/swift/Alias/IconProviderCallback" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk20IconProviderCallbacka" class="token"><code>IconProviderCallback</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A closure of this type can be provided as a callback to be invoked when an icon is received from the <a href="sdk-for-ios-navigate-classes-iconprovider">`IconProvider`</a> in the `UIImage` format. The callback provides information about the loaded icon, or an error if one occurred.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias IconProviderCallback = ( _ icon : UIImage ?, _ iconDescription : String ?, _ error : IconProviderError ?) -> Void
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
  <td><code> </code><em><code>icon</code></em><code> </code></td>
  <td><div>
  <p>The created icon, or <code>nil</code> if an error occurred.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>iconDescription</code></em><code> </code></td>
  <td><div>
  <p>An English description of the created icon. It will be <code>nil</code> if an error occurred.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>error</code></em><code> </code></td>
  <td><div>
  <p>The error that occurred, or <code>nil</code> if the icon is loaded successfully.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17IconProviderErrorO"></span>` `<span id="//apple_ref/swift/Enum/IconProviderError" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk17IconProviderErrorO" class="token"><code>IconProviderError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Error which indicates why an icon could not be retrieved.

  <a href="sdk-for-ios-navigate-enums-iconprovidererror" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum IconProviderError : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11ImageFormatO"></span>` `<span id="//apple_ref/swift/Enum/ImageFormat" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk11ImageFormatO" class="token"><code>ImageFormat</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Image format.

  <a href="sdk-for-ios-navigate-enums-imageformat" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum ImageFormat : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16JsonStyleFactoryC"></span>` `<span id="//apple_ref/swift/Class/JsonStyleFactory" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk16JsonStyleFactoryC" class="token"><code>JsonStyleFactory</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A factory of <a href="sdk-for-ios-navigate-classes-style">`Style`</a> objects from styles defined in JSON format. For more details see Custom Layer Style Reference in the documentation.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-jsonstylefactory" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class JsonStyleFactory
  ```

  ``` highlight
  extension JsonStyleFactory: NativeBase
  ```

  ``` highlight
  extension JsonStyleFactory: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk25KeyframeInterpolationModeO"></span>` `<span id="//apple_ref/swift/Enum/KeyframeInterpolationMode" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk25KeyframeInterpolationModeO" class="token"><code>KeyframeInterpolationMode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies type of interpolation performed between keyframes.

  <a href="sdk-for-ios-navigate-enums-keyframeinterpolationmode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum KeyframeInterpolationMode : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7LineCapO"></span>` `<span id="//apple_ref/swift/Enum/LineCap" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk7LineCapO" class="token"><code>LineCap</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Determines the cap (line ending) style.

  <a href="sdk-for-ios-navigate-enums-linecap" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum LineCap : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18LineTileDataSourceC"></span>` `<span id="//apple_ref/swift/Class/LineTileDataSource" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk18LineTileDataSourceC" class="token"><code>LineTileDataSource</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Line tile data source allows the rendering engine access to user managed data sets of geodetic lines and their attributes through a <a href="sdk-for-ios-navigate-protocols-linetilesource">`LineTileSource`</a>.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-linetiledatasource" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class LineTileDataSource
  ```

  ``` highlight
  extension LineTileDataSource: NativeBase
  ```

  ``` highlight
  extension LineTileDataSource: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14LineTileSourceP"></span>` `<span id="//apple_ref/swift/Protocol/LineTileSource" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk14LineTileSourceP" class="token"><code>LineTileSource</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A source of geodetic line tiles. Lines provided by an implementation must be clipped to the boundaries of the requested tile. The implementations must be thread-safe.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-protocols-linetilesource" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol LineTileSource : TileSource
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk31LineTileSourceLoadResultHandlerP"></span>` `<span id="//apple_ref/swift/Protocol/LineTileSourceLoadResultHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk31LineTileSourceLoadResultHandlerP" class="token"><code>LineTileSourceLoadResultHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Result handler of a load tile request.

  <a href="sdk-for-ios-navigate-protocols-linetilesourceloadresulthandler" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol LineTileSourceLoadResultHandler : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17LocationIndicatorC"></span>` `<span id="//apple_ref/swift/Class/LocationIndicator" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk17LocationIndicatorC" class="token"><code>LocationIndicator</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Graphical object to represent the location of the user on the map.

  It is either a green dot for pedestrian style or a triangular arrow for vehicle navigation style. This style can be changed by <a href="sdk-for-ios-navigate-classes-locationindicator#/s:7heresdk17LocationIndicatorC08locationC5StyleAC0cE0Ovp">`LocationIndicator.locationIndicatorStyle`</a>

  The location is made available to an instance of this class by calling

      LocationIndicator.updateLocation(Location)

  or
      LocationIndicator.updateLocation(Location, MapCameraUpdate)

  .
  </p>

  Use

      LocationIndicator.enable(...)

  to add this object to the map and
      LocationIndicator.disable(...)

  to remove it.
  </p>

  Note: The LocationIndicator is always rendered at a fixed altitude near 0. Changing the MapCamera to look at geographic coordinates with an altitude that is higher can cause the following behavior: If the MapCamera angle is tilted and altitude is too high, the LocationIndicator can unexpectedly disappear from the viewport due to the new perspective.

  <a href="sdk-for-ios-navigate-classes-locationindicator" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class LocationIndicator
  ```

  ``` highlight
  extension LocationIndicator: NativeBase
  ```

  ``` highlight
  extension LocationIndicator: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17LongPressDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/LongPressDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk17LongPressDelegateP" class="token"><code>LongPressDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol for handling long-press gestures. Long-press gesture occurs after tapping and holding the finger for a long time on the screen.

  <a href="sdk-for-ios-navigate-protocols-longpressdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol LongPressDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8MapArrowC"></span>` `<span id="//apple_ref/swift/Class/MapArrow" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk8MapArrowC" class="token"><code>MapArrow</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A visual representation of an arrow on the map. It consists of a tail - a polyline with an arbitrary number of points - and a head at its end.

  The map arrows are only visible on zoom levels \>= 13.

  Altitude component of <a href="sdk-for-ios-navigate-structs-geopolyline">`GeoPolyline`</a>‘s vertices is ignored.

  <a href="sdk-for-ios-navigate-classes-maparrow" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapArrow
  ```

  ``` highlight
  extension MapArrow: NativeBase
  ```

  ``` highlight
  extension MapArrow: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9MapCameraC"></span>` `<span id="//apple_ref/swift/Class/MapCamera" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk9MapCameraC" class="token"><code>MapCamera</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the camera looking onto the map view.

  Each map instance has exactly one camera that is used to manipulate the way the map is displayed.

  Any updates to the state of the camera will be applied while drawing the next map view frame and the current state of the camera reflects what is currently drawn inside the map view.

  Note: The camera can be configured and positioned even before a map scene is loaded for the first time. This allows for pre-setting the desired camera position, orientation, and zoom level, which will be applied once the map scene becomes available.

  **Camera Model**

  *Camera Concepts and Units*

  By default, HERE SDK uses an idealized Earth globe with a 3D-capable camera model. Being a 3D camera model means that the world position can be freely specified in geodetic 3D space (i.e. Earth centric) and the orientation can be freely changed around two axes - bearing (also known as head) and tilt (also known as pitch).

  The camera supports the look-at target with orientation on the ground way of setting up the camera in space. The camera is placed so that it looks at a specific geo-coordinates (placed at the `principal point`) from a given orientation and distance.

  - the look-at target in geo-coordinates (latitude, longitude) in degrees and an `altitude` in meters above MSL (mean sea level) at the `principal point`
  - the `orientation` at the look-at target
  - the distance of the camera from the look-at target, given as `distance` in meters or as `zoom-level`

  *Getting the current camera state*

  The current camera state can be obtained by the <a href="sdk-for-ios-navigate-classes-mapcamera#/s:7heresdk9MapCameraC5stateAC5StateVvp">`MapCamera.state`</a> call. It contains information about the camera look-at target (geo-coordinates and orientation) in geodetic space. The values are returned for the current `principal point`. This can lead to surprising or unexpected values in cases where the camera position/orientation was specified for another screen point, e.g. when using

      MapCameraUpdateFactory.lookAt(GeoBox)

  with a view rectangle, whose center does not coincide with the `principal point`. In this case, the geo-coordinates of the look-at target will differ from the center of the geo-box used in the `lookAt` call.
  </p>

  *Geo coordinates*

  Geo-coordinates are given in degrees and follow the common nomenclature of positive northern latitudes and positive eastern longitudes.

  *Altitude*

  When `altitude` is specified, it is always in meters above mean sea level (MSL). If this value is invalid (not-a-number) or not specified, then the terrain height at the given geo-coordinates will be looked up from the map. This is especially interesting in cases where terrain elevation is used within the map display.

  *Distance vs zoom-level vs scale*

  Map camera `distance, zoom-level` and `scale` determine how much of the world is visible on the HERE map. `Distance, zoom-level` and `scale` are directly connected and changing one will automatically change the others as well (except for `distance`/`scale` changes that map to `zoom-level` values \< 0 or \> 23).

  - `distance`: the distance from the camera to the look-at target on the surface of the Earth, in meters

  - `zoom-level`: the map zoom level, in the range \[0, 3\]. The relation between the width of the equator in logical pixels `w` and the zoom level `z` is:

        w = 256 * 2^(z)

  - `scale`: the scale of the map at the look-at target in meters on screen per meters on Earth. So a scale of 0.001 shows 10 meters on Earth within 1 cm on screen.

  The following mapping represents the `zoom-level` values:

  | zoom-level | ~ scale on screen (130dpi) | width of the equator in logical pixels | what can be seen |
  |----|:--:|:--:|:--:|
  | 0 | 1:800 million | 256 | Earth |
  | 1 | 1:400 million | 512 |  |
  | 2 | 1:200 million | 1024 |  |
  | 3 | 1:100 million | 2048 |  |
  | 4 | 1:50 million | 4096 | A continent |
  | 5 | 1:25 million | 8192 | Large roads |
  | 6 | 1:12 million | 16384 | Large rivers |
  | 7 | 1:6 million | 32768 | A country |
  | 8 | 1:3 million | 65536 |  |
  | 9 | 1:1 million | 131072 |  |
  | 10 | 1:780 thousand | 262144 |  |
  | 11 | 1:390 thousand | 524288 |  |
  | 12 | 1:195 thousand | 1048576 |  |
  | 13 | 1:100 thousand | 2097152 |  |
  | 14 | 1:50 thousand | 4194304 | A city |
  | 15 | 1:25 thousand | 8388608 |  |
  | 16 | 1:12 thousand | 16777216 | Buildings |
  | 17 | 1:6 thousand | 33554432 | Landmarks |
  | 18 | 1:3 thousand | 67108864 |  |
  | 19 | 1:1 thousand | 134217728 |  |
  | 20 | 1:7 hundred | 268435456 | Streets |
  | 21 | 1:3 hundred | 536870912 |  |
  | 22 | 1:1 hundred | 1073741824 |  |
  | 23 | 1:95 | 2147483648 |  |

  *Orientation*

  The camera `orientation` is composed of two parts:

  - `bearing`: also known as azimuth, the view direction in clockwise degrees; 0° = north, 90° = east, 180° = south, 270° = west
  - `tilt`: the angle in degrees from the vertical that the camera is looking down at the Earth; 0° = straight down.

  *Changing the Camera*

  All changes to the camera are encapsulated in camera updates that are created using the methods in the <a href="sdk-for-ios-navigate-classes-mapcameraupdatefactory">`MapCameraUpdateFactory`</a> class.

  These updates can then be applied to the <a href="sdk-for-ios-navigate-classes-heremap">`HereMap`</a> using

      MapCamera.applyUpdate(...)

  .
  </p>

  Camera updates are queued and executed when the next frame is rendered. They are executed in the order in which they were applied.

  *Animating the Camera*

  Camera updates can be animated by first creating a camera animation using the methods in the <a href="sdk-for-ios-navigate-classes-mapcameraanimationfactory">`MapCameraAnimationFactory`</a> class and then applying this animation to the <a href="sdk-for-ios-navigate-classes-heremap">`HereMap`</a> using

      MapCamera.startAnimation(MapCameraAnimation, AnimationDelegate)

  .
  </p>

  Only one camera animation for one camera component at a time is supported. Applying a new animation will cancel the active animation before the new one is started. The start position in this case is where ever the active animation happened to be at the time. Different components are camera state (`target pose` and `distance/zoom level/scale`) and camera projection (`field of view, focal length` and `principal point`).

  The running animations can also be canceled using

      MapCamera.cancelAnimations(...)

  or individual ones using
      MapCamera.cancelAnimation(...)

  .
  </p>

  <a href="sdk-for-ios-navigate-classes-mapcamera" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapCamera
  ```

  ``` highlight
  extension MapCamera: NativeBase
  ```

  ``` highlight
  extension MapCamera: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18MapCameraAnimationC"></span>` `<span id="//apple_ref/swift/Class/MapCameraAnimation" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk18MapCameraAnimationC" class="token"><code>MapCameraAnimation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An animation that can be applied to a <a href="sdk-for-ios-navigate-classes-mapcamera">`MapCamera`</a>. Creation is done via <a href="sdk-for-ios-navigate-classes-mapcameraanimationfactory">`MapCameraAnimationFactory`</a>.

  <a href="sdk-for-ios-navigate-classes-mapcameraanimation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapCameraAnimation
  ```

  ``` highlight
  extension MapCameraAnimation: NativeBase
  ```

  ``` highlight
  extension MapCameraAnimation: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk25MapCameraAnimationFactoryC"></span>` `<span id="//apple_ref/swift/Class/MapCameraAnimationFactory" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk25MapCameraAnimationFactoryC" class="token"><code>MapCameraAnimationFactory</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Factory for creating MapCameraAnimation objects to change map’s camera over time.

  <a href="sdk-for-ios-navigate-classes-mapcameraanimationfactory" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapCameraAnimationFactory
  ```

  ``` highlight
  extension MapCameraAnimationFactory: NativeBase
  ```

  ``` highlight
  extension MapCameraAnimationFactory: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17MapCameraDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/MapCameraDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk17MapCameraDelegateP" class="token"><code>MapCameraDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol for objects that want to get updates whenever the map is redrawn after camera parameters change.

  <a href="sdk-for-ios-navigate-protocols-mapcameradelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol MapCameraDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22MapCameraKeyframeTrackC"></span>` `<span id="//apple_ref/swift/Class/MapCameraKeyframeTrack" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk22MapCameraKeyframeTrackC" class="token"><code>MapCameraKeyframeTrack</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Stores keyframes for interpolation of a camera property using a specific easing function and interpolation mode. Can only hold keyframes of a single type.

  <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapCameraKeyframeTrack
  ```

  ``` highlight
  extension MapCameraKeyframeTrack: NativeBase
  ```

  ``` highlight
  extension MapCameraKeyframeTrack: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15MapCameraLimitsC"></span>` `<span id="//apple_ref/swift/Class/MapCameraLimits" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk15MapCameraLimitsC" class="token"><code>MapCameraLimits</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Controls constraints on map camera parameters.

  When constraints are set, they are enforced for current camera state and for all future changes to the camera.

  When setting, limits are applied on next rendering loop.

  <a href="sdk-for-ios-navigate-classes-mapcameralimits" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapCameraLimits
  ```

  ``` highlight
  extension MapCameraLimits: NativeBase
  ```

  ``` highlight
  extension MapCameraLimits: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15MapCameraUpdateC"></span>` `<span id="//apple_ref/swift/Class/MapCameraUpdate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk15MapCameraUpdateC" class="token"><code>MapCameraUpdate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An update that can be applied to the map camera. Creation is done via <a href="sdk-for-ios-navigate-classes-mapcameraupdatefactory">`MapCameraUpdateFactory`</a>.

  <a href="sdk-for-ios-navigate-classes-mapcameraupdate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapCameraUpdate
  ```

  ``` highlight
  extension MapCameraUpdate: NativeBase
  ```

  ``` highlight
  extension MapCameraUpdate: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22MapCameraUpdateFactoryC"></span>` `<span id="//apple_ref/swift/Class/MapCameraUpdateFactory" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk22MapCameraUpdateFactoryC" class="token"><code>MapCameraUpdateFactory</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Factory for creating MapCameraUpdate to change map’s camera.

  For some factory methods you can apply an additional padding in pixels by setting a `viewRectangle` parameter based on the current size of the map view:

  ``` highlight
  let leftPaddingInPixels = 5 let rightPaddingInPixels = 5 let topPaddingInPixels = 5 let bottomPaddingInPixels = 5 let horizontalPaddingInPixels = leftPaddingInPixels + rightPaddingInPixels let verticalPaddingInPixels = topPaddingInPixels + bottomPaddingInPixels let origin = Point2D ( leftPaddingInPixels , topPaddingInPixels ) let sizeInPixels = Size2D ( width : mapView . viewportSize . width - horizontalPaddingInPixels , height : mapView . viewportSize . height - verticalPaddingInPixels ) let paddedViewRectangle = Rectangle2D ( origin : origin , size : sizeInPixels )
  ```

  </pre>

  The origin indicates the top-left corner of the rectangle. An origin of (0, 0) indicates also the top-left corner of the map’s viewport.

  <a href="sdk-for-ios-navigate-classes-mapcameraupdatefactory" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapCameraUpdateFactory
  ```

  ``` highlight
  extension MapCameraUpdateFactory: NativeBase
  ```

  ``` highlight
  extension MapCameraUpdateFactory: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18MapContentCategoryO"></span>` `<span id="//apple_ref/swift/Enum/MapContentCategory" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk18MapContentCategoryO" class="token"><code>MapContentCategory</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Type representing map content categories.

  <a href="sdk-for-ios-navigate-enums-mapcontentcategory" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum MapContentCategory : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18MapContentSettingsC"></span>` `<span id="//apple_ref/swift/Class/MapContentSettings" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk18MapContentSettingsC" class="token"><code>MapContentSettings</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Provides settings regarding map data which are applied globally to all map views. The settings can already be changed before a map view instance is created.

  <a href="sdk-for-ios-navigate-classes-mapcontentsettings" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapContentSettings
  ```

  ``` highlight
  extension MapContentSettings: NativeBase
  ```

  ``` highlight
  extension MapContentSettings: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14MapContentTypeO"></span>` `<span id="//apple_ref/swift/Enum/MapContentType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk14MapContentTypeO" class="token"><code>MapContentType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Content types supported by the map.

  <a href="sdk-for-ios-navigate-enums-mapcontenttype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum MapContentType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10MapContextC"></span>` `<span id="//apple_ref/swift/Class/MapContext" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk10MapContextC" class="token"><code>MapContext</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  MapContext is the rendering engine and the context in which virtual geographic maps get rendered.

  It runs the render loop or offers the means for the user to run a custom one.

  Data sources, assets and virtual maps can be attached to the context. A virtual map can only render data from sources attached to the same context.

  The graphics backend to be used by the engine can be choosen by the user or a platform suitable one can be automatically selected internally. Only one graphics backend can be active and once selected it cannot be changed.

  <a href="sdk-for-ios-navigate-classes-mapcontext" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapContext
  ```

  ``` highlight
  extension MapContext: NativeBase
  ```

  ``` highlight
  extension MapContext: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8MapErrorO"></span>` `<span id="//apple_ref/swift/Enum/MapError" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk8MapErrorO" class="token"><code>MapError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents various errors that could occur from map related operations.

  <a href="sdk-for-ios-navigate-enums-maperror" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum MapError : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapFeaturesV"></span>` `<span id="//apple_ref/swift/Struct/MapFeatures" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk11MapFeaturesV" class="token"><code>MapFeatures</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Holds constants for map features, to be used with

      MapScene.enableFeatures(...)

  and
      MapScene.disableFeatures(...)

  .
  </p>

  See <a href="sdk-for-ios-navigate-structs-mapfeaturemodes">`MapFeatureModes`</a> for constants representing feature modes.

  <a href="sdk-for-ios-navigate-structs-mapfeatures" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct MapFeatures
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15MapFeatureModesV"></span>` `<span id="//apple_ref/swift/Struct/MapFeatureModes" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk15MapFeatureModesV" class="token"><code>MapFeatureModes</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Holds constants for map feature modes, to be used with

      MapScene.enableFeatures(...)

  .
  </p>

  Use <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV11defaultModeSSvpZ">`MapFeatureModes.defaultMode`</a> to enable a feature with its default mode.

  Note: The default mode is defined by the currently loaded map scene configuration and may vary per <a href="sdk-for-ios-navigate-enums-mapscheme">`MapScheme`</a>. The currently active features and modes can be inspected using

      MapScene.getActiveFeatures(...)

  after the scene is loaded.
  </p>

  See <a href="sdk-for-ios-navigate-structs-mapfeatures">`MapFeatures`</a> for constants representing the feature names.

  <a href="sdk-for-ios-navigate-structs-mapfeaturemodes" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct MapFeatureModes
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15MapIdleDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/MapIdleDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk15MapIdleDelegateP" class="token"><code>MapIdleDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Used to detect when the map becomes idle or busy.

  Map is considered busy when its state changes (for example as a result of camera manipulation) and/or when it requires a redraw (for example, as a result of map data being downloaded).

  Map is considered idle when current state is fully rendered and no further redraws are necessary.

  <a href="sdk-for-ios-navigate-protocols-mapidledelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol MapIdleDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8MapImageC"></span>` `<span id="//apple_ref/swift/Class/MapImage" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk8MapImageC" class="token"><code>MapImage</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a drawable resource that can be used by a <a href="sdk-for-ios-navigate-classes-mapmarker">`MapMarker`</a>, <a href="sdk-for-ios-navigate-classes-mapmarker3d">`MapMarker3D`</a> or <a href="sdk-for-ios-navigate-classes-mapimageoverlay">`MapImageOverlay`</a> to be shown on the map. Supported formats are listed in <a href="sdk-for-ios-navigate-enums-imageformat">`ImageFormat`</a>. SVG format allows custom fonts in text using font-family attribute by prior registration via `AssetsManager.registerFont`.

  It is recommended to associate a resource with a single `MapImage` instance in order to enable resource sharing and reduce the amount of needed memory.

  <a href="sdk-for-ios-navigate-classes-mapimage" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapImage
  ```

  ``` highlight
  extension MapImage: NativeBase
  ```

  ``` highlight
  extension MapImage: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15MapImageOverlayC"></span>` `<span id="//apple_ref/swift/Class/MapImageOverlay" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk15MapImageOverlayC" class="token"><code>MapImageOverlay</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  `MapImageOverlay` is used to draw images over the map, at a view coordinate inside the map viewport.

  The image to be displayed is represented by a <a href="sdk-for-ios-navigate-classes-mapimage">`MapImage`</a> object. By default, the overlay is centered on the given view coordinate.

  The resulting viewport area covered by the overlay is computed out of the overlay’s view coordinate, the anchor point and the image size. The overlay subareas that fall outside of the map viewport get clipped.

  To display the map overlay, it needs to be added to the scene using

      MapScene.addMapImageOverlay(...)

  . To stop displaying it, remove it from the scene using
      MapScene.removeMapImageOverlay(...)

  .
  </p>

  <a href="sdk-for-ios-navigate-classes-mapimageoverlay" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapImageOverlay
  ```

  ``` highlight
  extension MapImageOverlay: NativeBase
  ```

  ``` highlight
  extension MapImageOverlay: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20MapItemKeyFrameTrackC"></span>` `<span id="//apple_ref/swift/Class/MapItemKeyFrameTrack" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk20MapItemKeyFrameTrackC" class="token"><code>MapItemKeyFrameTrack</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Stores keyframes for interpolation of a map item property using a specific easing function and interpolation mode.

  The keyframe track object is used to create animations, see <a href="sdk-for-ios-navigate-classes-mapmarkeranimation">`MapMarkerAnimation`</a> and <a href="sdk-for-ios-navigate-classes-mappolylineanimation">`MapPolylineAnimation`</a>.

  <a href="sdk-for-ios-navigate-classes-mapitemkeyframetrack" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapItemKeyFrameTrack
  ```

  ``` highlight
  extension MapItemKeyFrameTrack: NativeBase
  ```

  ``` highlight
  extension MapItemKeyFrameTrack: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21MapItemRepresentationC"></span>` `<span id="//apple_ref/swift/Class/MapItemRepresentation" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk21MapItemRepresentationC" class="token"><code>MapItemRepresentation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Base class to represent visual style of particular map items.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapItemRepresentation
  ```

  ``` highlight
  extension MapItemRepresentation: NativeBase
  ```

  ``` highlight
  extension MapItemRepresentation: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8MapLayerC"></span>` `<span id="//apple_ref/swift/Class/MapLayer" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk8MapLayerC" class="token"><code>MapLayer</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Interface for managing a map layer. A map layer can be created by using the <a href="sdk-for-ios-navigate-classes-maplayerbuilder">`MapLayerBuilder`</a>. At creation, the layer gets added to a map. The layer gets removed from the map upon instance destruction.

  <a href="sdk-for-ios-navigate-classes-maplayer" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapLayer
  ```

  ``` highlight
  extension MapLayer: NativeBase
  ```

  ``` highlight
  extension MapLayer: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15MapLayerBuilderC"></span>` `<span id="//apple_ref/swift/Class/MapLayerBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk15MapLayerBuilderC" class="token"><code>MapLayerBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  MapLayerBuilder is used to add layers to a map to visualise a dataset in a programmatic way without defining it upfront in the configuration files.

  For example, after loading a scene configuration file, the renderer is setup to draw layers in the following order:

  - background
  - water
  - roads:outline
  - roads
  - labels

  Rendering order of elements in a single map layer can be controlled with categories. Layer names are unique, and category names have to be unique within a layer. The layer’s default, main category is unnamed.

  The concept of ‘category’ is tightly linked to styling. The idea behind category is that one should be able to style separately elements in a map layer. Take, for instance, roads. If one wants to style separately the bridges it will create a category ‘bridges’ and style it accordingly in the style file. If the user does not intend to or cannot style elements of the layer differently then it should opt for a layer with only the default category (e.g. for a raster layer, only the default category makes sense, since the layer has no other stylable elements apart from the raster image).

  A new layer called ‘zone’ and its category ‘background’ can be added dynamically so that the rendering order gets modified in the following way:

  - background
  - water
  - zone:background
  - zone
  - roads:outline
  - roads
  - labels

  This could be achieved with the help of the MapLayerPriorityBuilder and the MapLayerBuilder as in the following example:

  ``` highlight
  let layerPriority = MapLayerPriorityBuilder () . renderedAfterLayer ( named : "water" ) // places main category after 'water' . withCategory ( "background" ) . renderedAfterLayer ( named : "water" ) // places 'background' category after 'water' and before the // layer's main category. . build (); let layer = MapLayerBuilder () . withDataSource ( named : "DataSourceName" , contentType : MapContentType . line ) . forMap ( map ) . withName ( "zone" ) . withPriority ( layerPriority ) . build ();
  ```

  </pre>

  In case no layer priority or an empty one is provided, or if a reference layer-category pair is not present in the rendering order, the layer is going to be rendered last with respect to the rendering order at the time of its creation.

  Due to current limitations, the MapLayerPriority assignment is not implemented for point map layers. All labels will be rendered within the “labels” layer, defined in the scene configuration file. By default, all labels rendered by a point map layer are rendered last and no overlapping is allowed. The following categories can be used to have a different behaviour:

  - ‘custom-labels’ A label should be rendered first, is allowed to overlap with other labels of the same category and block map labels.
  - ‘custom-labels-no-self-overlap’ A label should be rendered after ‘custom-labels’, is not allowed to overlap with other labels of the same categoty and block map labels.
  - ‘custom-labels-overlap-all’ A label should be rendered last, is allowed to overlap all predefined categories, also map labels. These categories are configured accordingly in the basic map scene configurations. Category assignment to features can be done in the style based on data attributes. The category assignment can be done for all types of content: point, line, polygon.

  <a href="sdk-for-ios-navigate-classes-maplayerbuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapLayerBuilder
  ```

  ``` highlight
  extension MapLayerBuilder: NativeBase
  ```

  ``` highlight
  extension MapLayerBuilder: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16MapLayerPriorityC"></span>` `<span id="//apple_ref/swift/Class/MapLayerPriority" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk16MapLayerPriorityC" class="token"><code>MapLayerPriority</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  MapLayerPriority class. Instances are configured and created via a <a href="sdk-for-ios-navigate-classes-maplayerprioritybuilder">`MapLayerPriorityBuilder`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapLayerPriority
  ```

  ``` highlight
  extension MapLayerPriority: NativeBase
  ```

  ``` highlight
  extension MapLayerPriority: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23MapLayerPriorityBuilderC"></span>` `<span id="//apple_ref/swift/Class/MapLayerPriorityBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk23MapLayerPriorityBuilderC" class="token"><code>MapLayerPriorityBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  MapLayerPriorityBuilder is an interface used to define the rendering priority of a layer and its categories, relative to other layers or layer-category pairs.

  Map layers are rendered in an order according to specified priorities. Rendering order of elements in a single map layer can be controlled with categories. Layer names are unique, and category names have to be unique within a layer. The layer’s default, main category is unnamed.

  The concept of ‘category’ is tightly linked to styling. The idea behind category is that one should be able to style separately elements in a map layer. Take, for instance, roads. If one wants to style separately the bridges it will create a category ‘bridges’ and style it accordingly in the style file. If the user does not intend to or cannot style elements of the layer diffenrently then it should opt for a layer with only the default category (e.g. raster layer).

  One way to define layers’ priorities is by using a layer priority list in the scene configuration.

  For example, a priority list in a scene configuration could define:

  - background
  - water
  - roads:outline
  - roads
  - labels

  This means layer “background” is rendered first. Next up is layer “water”. Then category “outline” of layer “roads”, followed by the main category of layer “roads”. Layer “labels” is then rendered last.

  Now let’s consider a newly created layer ‘zone’ and its categories:

  - zone
  - zone:background
  - zone:lines-outline
  - zone:lines

  The user wants to alter the rendering order so that it looks like:

  - background
  - water
  - zone:background
  - zone
  - road:outline
  - road
  - zone:lines-outline
  - zone:lines
  - labels

  This could be achieved with the help of the MapLayerPriorityBuilder and a sequence of calls to its

      renderedBeforeLayer()

  and
      renderedAfterLayer()

  member functions.
  </p>

  Note that the order of calls matters and one can use a previously defined layer or category as a reference:

  ``` highlight
  let zoneLayerPriority = MapLayerPriorityBuilder () . renderedAfterLayer ( named : "water" ) // places "zone" after "water" // in the rendering order . withCategory ( named : "background" ) . renderedAfterLayer ( named : "water" ) // places "zone:background" after "water" // in the rendering order and thus shifts // "zone" to be rendered later . withCategory ( named : "lines-outline" ) . renderedAfterLayer ( named : "road" ) // places "zone:lines-outline" after "road" // in the rendering order . withCategory ( named : "lines" ) . renderedAfterLayer ( named : "zone" , categoryName : "lines-outline" ) // places "zone:lines" after // "zone:lines-outline" in the rendering order . build (); zoneLayer . setPriority ( zoneLayerPriority ); // applies the priority to the zone layer // and its categories in one single operation.
  ```

  </pre>

  In case an empty MapLayerPriority without any ordering commands is built, it is assumed that the target layer is going to be rendered last.

  Due to a current limitation for point map layers, the mentioned APIs to control the rendering order are not implemented. All labels will be rendered within the “labels” layer, defined in the scene configuration file. By default, all labels rendered by a point map layer are rendered last and no overlapping is allowed. The following categories can be used to have a different behaviour:

  - ‘custom-labels’ A label should be rendered first, is allowed to overlap with other labels of the same category and block map labels.
  - ‘custom-labels-no-self-overlap’ A label should be rendered after ‘custom-labels’, is not allowed to overlap with other labels of the same categoty and block map labels.
  - ‘custom-labels-overlap-all’ A label should be rendered last, is allowed to overlap all predefined categories, also map labels. These categories are configured accordingly in the basic map scene configurations. Category assignment to features can be done in the style based on data attributes. The category assignment can be done for all types of data: points, lines, polygons.

  <a href="sdk-for-ios-navigate-classes-maplayerprioritybuilder" class="slightly-smaller">See more</a>
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapLayerPriorityBuilder
  ```

  ``` highlight
  extension MapLayerPriorityBuilder: NativeBase
  ```

  ``` highlight
  extension MapLayerPriorityBuilder: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk08MapLayerB29MeasureDependentStorageLevelsC"></span>` `<span id="//apple_ref/swift/Class/MapLayerMapMeasureDependentStorageLevels" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk08MapLayerB29MeasureDependentStorageLevelsC" class="token"><code>MapLayerMapMeasureDependentStorageLevels</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Provides a mapping between a MapLayer map measure to datasource storage level.

  <a href="sdk-for-ios-navigate-classes-maplayermapmeasuredependentstoragelevels" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapLayerMapMeasureDependentStorageLevels
  ```

  ``` highlight
  extension MapLayerMapMeasureDependentStorageLevels: NativeBase
  ```

  ``` highlight
  extension MapLayerMapMeasureDependentStorageLevels: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23MapLayerVisibilityRangeV"></span>` `<span id="//apple_ref/swift/Struct/MapLayerVisibilityRange" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk23MapLayerVisibilityRangeV" class="token"><code>MapLayerVisibilityRange</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A layer’s visibility along a zoom level range. The range is half open - \<a href="sdk-for-ios-navigate-classes-mapsceneloadoptionsbuilder">minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.

  <a href="sdk-for-ios-navigate-structs-maplayervisibilityrange" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct MapLayerVisibilityRange : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16MapMarkerClusterC"></span>` `<span id="//apple_ref/swift/Class/MapMarkerCluster" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk16MapMarkerClusterC" class="token"><code>MapMarkerCluster</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Groups map markers and enables their clustering to reduce visual clutter when there are many of them in a small area.

  The markers that are close to each other are replaced by a single cluster marker. Cluster groups are generated based on geographical distance between objects, not based on screen space collision. Hence it is possible, that cluster markers can overlap.

  The markers can be added to a cluster or to a scene, but not to both. To display the cluster on the map, add it to the scene using

      MapScene.addMapMarkerCluster(...)

  . The display of a cluster is only guaranteed in case its origin is within the viewport. At the moment, this is a known limitation that mostly affects clusters which are visually large and cover a sizeable part of the viewport.
  </p>

  Markers part of the cluster with opacity set to zero are still on the map and are considered for picking and clustering.

  <a href="sdk-for-ios-navigate-classes-mapmarkercluster" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapMarkerCluster
  ```

  ``` highlight
  extension MapMarkerCluster: NativeBase
  ```

  ``` highlight
  extension MapMarkerCluster: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15MapMeasureRangeV"></span>` `<span id="//apple_ref/swift/Struct/MapMeasureRange" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk15MapMeasureRangeV" class="token"><code>MapMeasureRange</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A map measure range.

  <a href="sdk-for-ios-navigate-structs-mapmeasurerange" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct MapMeasureRange : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19MapObjectDescriptorC"></span>` `<span id="//apple_ref/swift/Class/MapObjectDescriptor" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk19MapObjectDescriptorC" class="token"><code>MapObjectDescriptor</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Interface represents descriptor of a pickable map object.

  <a href="sdk-for-ios-navigate-classes-mapobjectdescriptor" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapObjectDescriptor
  ```

  ``` highlight
  extension MapObjectDescriptor: NativeBase
  ```

  ``` highlight
  extension MapObjectDescriptor: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13MapProjectionO"></span>` `<span id="//apple_ref/swift/Enum/MapProjection" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk13MapProjectionO" class="token"><code>MapProjection</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The map projection used for rendering.

  <a href="sdk-for-ios-navigate-enums-mapprojection" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum MapProjection : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14MapSceneLightsC"></span>` `<span id="//apple_ref/swift/Class/MapSceneLights" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk14MapSceneLightsC" class="token"><code>MapSceneLights</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Manage the lights and their attributes in a scene.

  <a href="sdk-for-ios-navigate-classes-mapscenelights" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapSceneLights
  ```

  ``` highlight
  extension MapSceneLights: NativeBase
  ```

  ``` highlight
  extension MapSceneLights: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19MapSceneLoadOptionsC"></span>` `<span id="//apple_ref/swift/Class/MapSceneLoadOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk19MapSceneLoadOptionsC" class="token"><code>MapSceneLoadOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the configuration options for loading a map scene. This class combines both the scene source (MapScheme or configuration file) and optional settings like features, watermark style and overriding map style.

  It is left empty intentionally. Use [`MapSceneLoadOptionsBuilder`</a> to create instances of this class.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapSceneLoadOptions
  ```

  ``` highlight
  extension MapSceneLoadOptions: NativeBase
  ```

  ``` highlight
  extension MapSceneLoadOptions: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk26MapSceneLoadOptionsBuilderC"></span>` `<span id="//apple_ref/swift/Class/MapSceneLoadOptionsBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk26MapSceneLoadOptionsBuilderC" class="token"><code>MapSceneLoadOptionsBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Builder for creating <a href="sdk-for-ios-navigate-maps#/s:7heresdk19MapSceneLoadOptionsC">`MapSceneLoadOptions`</a> instances. This builder ensures that either a MapScheme or a configuration file is set, but not both.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-mapsceneloadoptionsbuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapSceneLoadOptionsBuilder
  ```

  ``` highlight
  extension MapSceneLoadOptionsBuilder: NativeBase
  ```

  ``` highlight
  extension MapSceneLoadOptionsBuilder: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9MapMarkerC"></span>` `<span id="//apple_ref/swift/Class/MapMarker" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk9MapMarkerC" class="token"><code>MapMarker</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  `MapMarker` is used to draw images on the map, for example to mark a specific location. By default, the marker is centered on the given geographic coordinates. Markers keep their size regardless of the current zoom level of the map view.

  The image to be displayed is represented by <a href="sdk-for-ios-navigate-classes-mapimage">`MapImage`</a> object. For performance reasons, it is highly recommended to reuse a single instance of the image when creating multiple identical markers.

  To display the map marker, it needs to be added to the scene using

      MapScene.addMapMarker(...)

  . To stop displaying it, remove it from the scene using
      MapScene.removeMapMarker(...)

  .
  </p>

  The display of a map marker is only guaranteed in case its origin is within the viewport. At the moment, this is a known limitation that mostly affects map markers which are visually large and cover a sizeable part of the viewport.

  **Note:** Due to technical limitations using the MapMarkers API to add a very large number of markers (several thousands, especially 10000+) is not recommended. Adding this many markers will have a negative impact on the performance leading to stuttering of the app and lower frame rates. To work around this limitation the following approach can be used: Register to map camera updates using

      MapCamera.addDelegate(...)

  . Query the bounding box of the camera viewport using <a href="sdk-for-ios-navigate-classes-mapcamera#/s:7heresdk9MapCameraC11boundingBoxAA03GeoE0VSgvp">`MapCamera.boundingBox`</a> (it may be extended) and then use the method
      GeoBox.contains(GeoCoordinates)

  in combination with <a href="sdk-for-ios-navigate-classes-mapcamera-state#/s:7heresdk9MapCameraC5StateV24distanceToTargetInMetersSdvp">`MapCamera.State.distanceToTargetInMeters`</a> to determine which MapMarkers are actually visible to the user in the current camera viewport and thus need to be added to the map.
  </p>

  <a href="sdk-for-ios-navigate-classes-mapmarker" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapMarker
  ```

  ``` highlight
  extension MapMarker: NativeBase
  ```

  ``` highlight
  extension MapMarker: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapMarker3DC"></span>` `<span id="//apple_ref/swift/Class/MapMarker3D" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk11MapMarker3DC" class="token"><code>MapMarker3D</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a 3D shape drawn on the map at specified geodetic coordinates.

  It can have a solid color or be textured, depending on the data from <a href="sdk-for-ios-navigate-classes-mapmarker3dmodel">`MapMarker3DModel`</a>.

  By default, a 3D marker is drawn on top of all map content, including 3D map elements like extruded buildings or 3D landmarks. This can be changed by enabling depth check using <a href="sdk-for-ios-navigate-classes-mapmarker3d#/s:7heresdk11MapMarker3DC19isDepthCheckEnabledSbvp">`MapMarker3D.isDepthCheckEnabled`</a>.

  The display of a 3D marker is only guaranteed in case its origin is within the viewport. At the moment, this is a known limitation that mostly affects a 3D marker that is visually large and covers a sizeable part of the viewport.

  # Sizing and scaling

  Two aspects determine how big the `MapMarker3D` will be on the screen and how will it behave when the map is zoomed in and out.

  The first, and most impactful is <a href="sdk-for-ios-navigate-structs-rendersize-unit">`RenderSize.Unit`</a>, which specifies how the vertex coordinates of the 3D model are interpreted. Most importantly, it specifies whether the 3D model is placed in world or screen coordinate space.

  <a href="sdk-for-ios-navigate-structs-rendersize-unit#/s:7heresdk10RenderSizeV4UnitO6metersyA2EmF">`RenderSize.Unit.meters`</a> will make the 3D model use world coordinate space, meaning that it will change size together with the map when it is zoomed in and out.

  <a href="sdk-for-ios-navigate-structs-rendersize-unit#/s:7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">`RenderSize.Unit.pixels`</a> makes the 3D model use screen coordinate space, meaning that it will have constant size on the screen regardless of how the map zoom changes. So a simple 10 by 10 (in model space) rectangle will have a size of 10 by 10 pixels on the screen.

  <a href="sdk-for-ios-navigate-structs-rendersize-unit#/s:7heresdk10RenderSizeV4UnitO24densityIndependentPixelsyA2EmF">`RenderSize.Unit.densityIndependentPixels`</a> is similar to pixels, but the resulting size will take into account the pixel density of the display, meaning that physical size on the screen will be approximately the same regardless of the size or resolution of the display.

  The second aspect that determines size of `MapMarker3D` is scale. It can be specified at construction time and can be changed later at any time using <a href="sdk-for-ios-navigate-classes-mapmarker3d#/s:7heresdk11MapMarker3DC5scaleSdvp">`MapMarker3D.scale`</a>.

  # Modifying at runtime

  A 3D marker can be moved around a map by updating its coordinates using <a href="sdk-for-ios-navigate-classes-mapmarker3d#/s:7heresdk11MapMarker3DC11coordinatesAA14GeoCoordinatesVvp">`MapMarker3D.coordinates`</a>.

  Altitude component of the coordinates, if set, controls 3D marker’s elevation above ground. If not set, the 3D marker is placed at ground level.

  Its orientation is specified by bearing, pitch and roll and can be changed by using <a href="sdk-for-ios-navigate-classes-mapmarker3d#/s:7heresdk11MapMarker3DC7bearingSdvp">`MapMarker3D.bearing`</a>, <a href="sdk-for-ios-navigate-classes-mapmarker3d#/s:7heresdk11MapMarker3DC5pitchSdvp">`MapMarker3D.pitch`</a> and <a href="sdk-for-ios-navigate-classes-mapmarker3d#/s:7heresdk11MapMarker3DC4rollSdvp">`MapMarker3D.roll`</a>.

  # Flat marker

  A flat marker is a special case of a 3D marker, where the 3D shape being drawn is a simple textured rectangle. In essence it’s an image drawn “on the ground”. Such 3D marker can be conveniently created using

      MapMarker3D.init(GeoCoordinates, MapImage, Double, RenderSize.Unit)

  constructor. Of course, once created, it can be rotated to face any direction.
  </p>

  <a href="sdk-for-ios-navigate-classes-mapmarker3d" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapMarker3D
  ```

  ``` highlight
  extension MapMarker3D: NativeBase
  ```

  ``` highlight
  extension MapMarker3D: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16MapMarker3DModelC"></span>` `<span id="//apple_ref/swift/Class/MapMarker3DModel" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk16MapMarker3DModelC" class="token"><code>MapMarker3DModel</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a 3D model that can be used by a <a href="sdk-for-ios-navigate-classes-mapmarker3d">`MapMarker3D`</a> to be shown on the map. Geometry of 3D marker can be provided in form of a Wavefront OBJ file as specified in <http://www.martinreddy.net/gfx/3d/OBJ.spec> or as mesh built via <a href="sdk-for-ios-navigate-classes-meshbuilder">`MeshBuilder`</a>.

  # 1. Creating `MapMarker3DModel` from OBJ file

  For OBJ files, HERE SDK only supports the following set of features of the OBJ specification:

  - Triangle Meshes
  - Following vertex attributes must be present:
    - Vertex Position
    - Vertex Normal
    - Texture Coordinates
    - Geometry must be indexed (contain an Index Buffer)
    - Face element

  HERE SDK does not support:

  - Multi Texturing
  - Materials (mtllib \[external .mtl file name\] )
    - Lines
    - Higher Order Surfaces
    - Vendor specific extensions

  For supported texture formats, HERE SDK allows the following formats to be specified: JPG, PNG, GPU compressed texture formats: ECT1 (OpenGL only), YUV, ASTC, KTX.

  # 2. Creating `MapMarker3DModel` programatically

  A 3D mesh can be specified programatically using <a href="sdk-for-ios-navigate-classes-meshbuilder">`MeshBuilder`</a> and passed to `MapMarker3DModel` constructor. This method supports creating a mesh from quads and triangles. Textured geometry is also supported, the mesh faces need to have texture coordinates and a texture file needs to be passed along with the mesh to `MapMarker3DModel` constructor.

  <a href="sdk-for-ios-navigate-classes-mapmarker3dmodel" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapMarker3DModel
  ```

  ``` highlight
  extension MapMarker3DModel: NativeBase
  ```

  ``` highlight
  extension MapMarker3DModel: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18MapMarkerAnimationC"></span>` `<span id="//apple_ref/swift/Class/MapMarkerAnimation" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk18MapMarkerAnimationC" class="token"><code>MapMarkerAnimation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An animation that can be applied to the <a href="sdk-for-ios-navigate-classes-mapmarker">`MapMarker`</a> object.

  <a href="sdk-for-ios-navigate-classes-mapmarkeranimation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapMarkerAnimation
  ```

  ``` highlight
  extension MapMarkerAnimation: NativeBase
  ```

  ``` highlight
  extension MapMarkerAnimation: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10MapMeasureV"></span>` `<span id="//apple_ref/swift/Struct/MapMeasure" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk10MapMeasureV" class="token"><code>MapMeasure</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A map measure. Check <a href="sdk-for-ios-navigate-classes-mapcamera">`MapCamera`</a> for more details on each supported measure.

  <a href="sdk-for-ios-navigate-structs-mapmeasure" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct MapMeasure : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk29MapMeasureDependentRenderSizeV"></span>` `<span id="//apple_ref/swift/Struct/MapMeasureDependentRenderSize" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk29MapMeasureDependentRenderSizeV" class="token"><code>MapMeasureDependentRenderSize</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a render size, described as map measure dependent values.

  <a href="sdk-for-ios-navigate-structs-mapmeasuredependentrendersize" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct MapMeasureDependentRenderSize : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10MapPolygonC"></span>` `<span id="//apple_ref/swift/Class/MapPolygon" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk10MapPolygonC" class="token"><code>MapPolygon</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A visual representation of a polygon on the map. Can be used to visualize areas of all shapes and sizes.

  The geometry to be visualized is represented by an instance of <a href="sdk-for-ios-navigate-structs-geopolygon">`GeoPolygon`</a>. To display circular areas (for example, a position accuracy indicator) use a GeoPolygon created from a <a href="sdk-for-ios-navigate-structs-geocircle">`GeoCircle`</a> using

      GeoPolygon.init(GeoCircle)

  .
  </p>

  Note:

  - The polygon shape should not cover more than half of the globe, otherwise unexpected results may occur.
  - Polygons which are self-intersecting are not supported and may lead to render artifacts.
  - The inner boundaries (holes) specified in the GeoPolygon are ignored.

  <a href="sdk-for-ios-navigate-classes-mappolygon" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapPolygon
  ```

  ``` highlight
  extension MapPolygon: NativeBase
  ```

  ``` highlight
  extension MapPolygon: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapPolylineC"></span>` `<span id="//apple_ref/swift/Class/MapPolyline" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk11MapPolylineC" class="token"><code>MapPolyline</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A visual representation of a line on the map.

  The geometry to be visualized is represented by an instance of <a href="sdk-for-ios-navigate-structs-geopolyline">`GeoPolyline`</a>.

  Altitude component of <a href="sdk-for-ios-navigate-structs-geopolyline">`GeoPolyline`</a>‘s vertices is ignored.

  <a href="sdk-for-ios-navigate-classes-mappolyline" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapPolyline
  ```

  ``` highlight
  extension MapPolyline: NativeBase
  ```

  ``` highlight
  extension MapPolyline: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20MapPolylineAnimationC"></span>` `<span id="//apple_ref/swift/Class/MapPolylineAnimation" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk20MapPolylineAnimationC" class="token"><code>MapPolylineAnimation</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An animation that can be applied to the <a href="sdk-for-ios-navigate-classes-mappolyline">`MapPolyline`</a> object.

  <a href="sdk-for-ios-navigate-classes-mappolylineanimation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapPolylineAnimation
  ```

  ``` highlight
  extension MapPolylineAnimation: NativeBase
  ```

  ``` highlight
  extension MapPolylineAnimation: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13MapPickResultC"></span>` `<span id="//apple_ref/swift/Class/MapPickResult" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk13MapPickResultC" class="token"><code>MapPickResult</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A class representing a map pick result.

  <a href="sdk-for-ios-navigate-classes-mappickresult" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapPickResult
  ```

  ``` highlight
  extension MapPickResult: NativeBase
  ```

  ``` highlight
  extension MapPickResult: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8MapSceneC"></span>` `<span id="//apple_ref/swift/Class/MapScene" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk8MapSceneC" class="token"><code>MapScene</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a map scene and exposes the functionality to manipulate its content.

  ## Map schemes

  The content of the displayed map and how it looks is specified by a <a href="sdk-for-ios-navigate-enums-mapscheme">`MapScheme`</a> which is set when loading a scene with

      MapScene.loadScene(MapScheme, MapScene.LoadSceneCompletionHandler?)

  . It is also possible to load your own custom map scheme from a file bundled with your application. Supported file formats are:
  </p>

  - JSON (file extension ‘.json’; e.g. ‘my_custom_style.json’)
  - ZIP archive (file extension ‘.zip’; e.g. ‘my_custom_style.zip’), with the following archive structure:
    - root folder: any, not empty (e.g. ‘my_custom_style’)
    - JSON configuration: ‘<root folder>/style.json’</root>
    - custom assets folder: ‘<root folder>/assets’</root>

  ## Map features

  Different map schemes offer different sets of features, for example showing traffic or 3D buildings. Some features have multiple modes of operation, but most have only one.

      MapScene.getSupportedFeatures(...)

  can be used to check what features and modes are supported for the current scene. Features can be enabled using
      MapScene.enableFeatures(...)

  and disabled with
      MapScene.disableFeatures(...)

  . Checking which features are currently enabled can be done using
      MapScene.getActiveFeatures(...)

  . For convenience, <a href="sdk-for-ios-navigate-structs-mapfeatures">`MapFeatures`</a> and <a href="sdk-for-ios-navigate-structs-mapfeaturemodes">`MapFeatureModes`</a> hold constants for feature and mode names.
  </p>

  Since version 4.15.0, map features cannot be controlled using

      MapScene.setLayerVisibility(...)

  , since
      MapScene.setLayerVisibility(...)

  controls only visibility of the layers which are corresponding to the features enabled either by
      MapScene.enableFeatures(...)

  or enabled by default for the scene.
  </p>

  ## Map layers

  A map scheme is organized in layers, which can be controlled using

      MapScene.setLayerVisibility(...)

  . It’s possible to change the visibility state of any map layer as long as the name is known.
  </p>

  Layer visibility settings persist between scene reloading.

  ## User content

  User generated content can be visualised on the map using <a href="sdk-for-ios-navigate-classes-mappolyline">`MapPolyline`</a>, <a href="sdk-for-ios-navigate-classes-mappolygon">`MapPolygon`</a>, <a href="sdk-for-ios-navigate-classes-mapmarker">`MapMarker`</a>, <a href="sdk-for-ios-navigate-classes-mapmarkercluster">`MapMarkerCluster`</a>, <a href="sdk-for-ios-navigate-classes-maparrow">`MapArrow`</a>, <a href="sdk-for-ios-navigate-classes-mapmarker3d">`MapMarker3D`</a> and <a href="sdk-for-ios-navigate-classes-mapimageoverlay">`MapImageOverlay`</a> (collectively referred to as “map items”). Those can be added to and removed from the scene by respective add and remove methods. The render order of the map items is according to the list above. The order of objects within the same type can be controlled using the `drawOrder` property of each object.

  Be careful when adding a very large number of map items as this can have a negative impact on the performance of the app. To work around this limitation the following approach can be used: Register to map camera updates using

      MapCamera.addDelegate(...)

  . Query the bounding box of the camera viewport using <a href="sdk-for-ios-navigate-classes-mapcamera#/s:7heresdk9MapCameraC11boundingBoxAA03GeoE0VSgvp">`MapCamera.boundingBox`</a> (it may be extended) and then use the method
      GeoBox.contains(GeoCoordinates)

  in combination with <a href="sdk-for-ios-navigate-classes-mapcamera-state#/s:7heresdk9MapCameraC5StateV24distanceToTargetInMetersSdvp">`MapCamera.State.distanceToTargetInMeters`</a> to determine which map items are actually visible to the user in the current camera viewport and thus need to be added to the map.
  </p>

  <a href="sdk-for-ios-navigate-classes-mapscene" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapScene
  ```

  ``` highlight
  extension MapScene: NativeBase
  ```

  ``` highlight
  extension MapScene: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9MapSchemeO"></span>` `<span id="//apple_ref/swift/Enum/MapScheme" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk9MapSchemeO" class="token"><code>MapScheme</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the preconfigured map schemes bundled with the SDK.

  <a href="sdk-for-ios-navigate-enums-mapscheme" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum MapScheme : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapViewBaseP"></span>` `<span id="//apple_ref/swift/Protocol/MapViewBase" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk11MapViewBaseP" class="token"><code>MapViewBase</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the available public API from <a href="sdk-for-ios-navigate-classes-mapview">`MapView`</a>.

  <a href="sdk-for-ios-navigate-protocols-mapviewbase" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol MapViewBase : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/c:@M@heresdk@objc(cs)HereMapView"></span>` `<span id="//apple_ref/swift/Class/MapView" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/c:@M@heresdk@objc(cs)HereMapView" class="token"><code>MapView</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A view that displays a map. Note: Before using this class, <a href="sdk-for-ios-navigate-classes-sdknativeengine">`SDKNativeEngine`</a> must be already initialized.

  <a href="sdk-for-ios-navigate-classes-mapview" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @IBDesignable @objc(HereMapView) @MainActor open class MapView : UIView , MapViewBase
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24MapViewLifecycleDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/MapViewLifecycleDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk24MapViewLifecycleDelegateP" class="token"><code>MapViewLifecycleDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Provides a mechanism for observing a lifecycle of a map view and/or implementing components whose lifecycle needs to be linked with that of a map view.

  Storing the map view in a strong reference is strongly discouraged, as that will create a reference cycle and prevent map view from being released.

  A <a href="sdk-for-ios-navigate-classes-mapview">`MapView`</a> is using a <a href="https://developer.apple.com/documentation/quartzcore/cametallayer">CAMetalLayer</a>

  to render its content.

  <a href="sdk-for-ios-navigate-protocols-mapviewlifecycledelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol MapViewLifecycleDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14MapViewOptionsV"></span>` `<span id="//apple_ref/swift/Struct/MapViewOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk14MapViewOptionsV" class="token"><code>MapViewOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Options used for initialization of map view

  <a href="sdk-for-ios-navigate-structs-mapviewoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct MapViewOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20MaterialReflectivityV"></span>` `<span id="//apple_ref/swift/Struct/MaterialReflectivity" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk20MaterialReflectivityV" class="token"><code>MaterialReflectivity</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Material reflectivity properties are used to enable per‑pixel lighting for supported map objects (e.g. <a href="sdk-for-ios-navigate-classes-locationindicator">`LocationIndicator`</a> markers and their halo).

  ## Lighting OFF vs ON

  By default (when no MaterialReflectivity is assigned) objects are rendered “unlit” (emissive): their texture / color appears at a constant brightness, unaffected by scene lights. Assigning a `MaterialReflectivity` instance to an object that supports it (e.g. <a href="sdk-for-ios-navigate-classes-locationindicator#/s:7heresdk17LocationIndicatorC20materialReflectivityAA08MaterialE0VSgvp">`LocationIndicator.materialReflectivity`</a>) automatically enables lighting for this object and all its internal components. Clearing (setting the property to `nil`) disables lighting again and restores the unlit appearance.

  ## Factors

  Both factors are expected to be within \[0.0, 1.0\]. Values outside this range are allowed but may produce exaggerated results or be clamped by future implementations. Typical useful ranges:

  - ambientFactor: 0.0 – 0.4 (higher values flatten the shading and reduce directional contrast)
  - diffuseFactor: 0.5 – 1.0 (lower values dim the object under directional light)

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-materialreflectivity" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct MaterialReflectivity : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk4MeshC"></span>` `<span id="//apple_ref/swift/Class/Mesh" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk4MeshC" class="token"><code>Mesh</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a mesh in 3D space. Such meshes are built using <a href="sdk-for-ios-navigate-classes-meshbuilder">`MeshBuilder`</a>.

  The class is not offering any methods, as its data is only meant to be consumed internally when being passed to <a href="sdk-for-ios-navigate-classes-mapmarker3dmodel">`MapMarker3DModel`</a> constructor.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class Mesh
  ```

  ``` highlight
  extension Mesh: NativeBase
  ```

  ``` highlight
  extension Mesh: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MeshBuilderC"></span>` `<span id="//apple_ref/swift/Class/MeshBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk11MeshBuilderC" class="token"><code>MeshBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Builder for meshes. Such meshes can contain different kinds of primitives, like quads or triangles. Both primitives support adding texture coordinates that are mapped to the corners of the primitives. See <a href="sdk-for-ios-navigate-classes-trianglemeshbuilder">`TriangleMeshBuilder`</a> and <a href="sdk-for-ios-navigate-classes-quadmeshbuilder">`QuadMeshBuilder`</a> for more details.

  Note: Normals cannot be set as they are not necessary when using the `MeshBuilder`.

  **Example how to build a cube using <a href="sdk-for-ios-navigate-classes-quadmeshbuilder">`QuadMeshBuilder`</a>**

  ``` highlight
  let cube = MeshBuilder () . quad ( a : Point3D ( x : 0.5 , y : 0.5 , z : 0.5 ), b : Point3D ( x : - 0.5 , y : 0.5 , z : 0.5 ), c : Point3D ( x : 0.5 , y : - 0.5 , z : 0.5 ), d : Point3D ( x : - 0.5 , y : - 0.5 , z : 0.5 )) . quad ( a : Point3D ( x : - 0.5 , y : 0.5 , z : - 0.5 ), b : Point3D ( x : 0.5 , y : 0.5 , z : - 0.5 ), c : Point3D ( x : - 0.5 , y : - 0.5 , z : - 0.5 ), d : Point3D ( x : 0.5 , y : - 0.5 , z : - 0.5 )) . quad ( a : Point3D ( x : 0.5 , y : 0.5 , z : - 0.5 ), b : Point3D ( x : 0.5 , y : 0.5 , z : 0.5 ), c : Point3D ( x : 0.5 , y : - 0.5 , z : - 0.5 ), d : Point3D ( x : 0.5 , y : - 0.5 , z : 0.5 )) . quad ( a : Point3D ( x : - 0.5 , y : 0.5 , z : 0.5 ), b : Point3D ( x : - 0.5 , y : 0.5 , z : - 0.5 ), c : Point3D ( x : - 0.5 , y : - 0.5 , z : 0.5 ), d : Point3D ( x : - 0.5 , y : - 0.5 , z : - 0.5 )) . quad ( a : Point3D ( x : - 0.5 , y : 0.5 , z : 0.5 ), b : Point3D ( x : 0.5 , y : 0.5 , z : 0.5 ), c : Point3D ( x : - 0.5 , y : 0.5 , z : - 0.5 ), d : Point3D ( x : 0.5 , y : 0.5 , z : - 0.5 )) . quad ( a : Point3D ( x : 0.5 , y : - 0.5 , z : 0.5 ), b : Point3D ( x : - 0.5 , y : - 0.5 , z : 0.5 ), c : Point3D ( x : 0.5 , y : - 0.5 , z : - 0.5 ), d : Point3D ( x : - 0.5 , y : - 0.5 , z : - 0.5 )) . build ()
  ```

  </pre>

  <a href="sdk-for-ios-navigate-classes-meshbuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MeshBuilder
  ```

  ``` highlight
  extension MeshBuilder: NativeBase
  ```

  ``` highlight
  extension MeshBuilder: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11PanDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/PanDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk11PanDelegateP" class="token"><code>PanDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol for handling pan gestures. Pan gesture occurs when a finger is moving on the screen.

  <a href="sdk-for-ios-navigate-protocols-pandelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol PanDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20PickMapContentResultC"></span>` `<span id="//apple_ref/swift/Class/PickMapContentResult" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk20PickMapContentResultC" class="token"><code>PickMapContentResult</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A class that contains possible results from picking map content on the map scene.

  <a href="sdk-for-ios-navigate-classes-pickmapcontentresult" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class PickMapContentResult
  ```

  ``` highlight
  extension PickMapContentResult: NativeBase
  ```

  ``` highlight
  extension PickMapContentResult: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18PickMapItemsResultC"></span>` `<span id="//apple_ref/swift/Class/PickMapItemsResult" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk18PickMapItemsResultC" class="token"><code>PickMapItemsResult</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Carries results from the picking of map items on the map scene.

  <a href="sdk-for-ios-navigate-classes-pickmapitemsresult" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class PickMapItemsResult
  ```

  ``` highlight
  extension PickMapItemsResult: NativeBase
  ```

  ``` highlight
  extension PickMapItemsResult: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19PinchRotateDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/PinchRotateDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk19PinchRotateDelegateP" class="token"><code>PinchRotateDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol for handling pinch rotate gestures. Pinch rotate gesture occurs when two fingers are on the screen and at least one of them moves.

  <a href="sdk-for-ios-navigate-protocols-pinchrotatedelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol PinchRotateDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9PointDataC"></span>` `<span id="//apple_ref/swift/Class/PointData" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk9PointDataC" class="token"><code>PointData</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a geodetic point with custom attributes. Can be created using a <a href="sdk-for-ios-navigate-classes-pointdatabuilder">`PointDataBuilder`</a>.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class PointData
  ```

  ``` highlight
  extension PointData: NativeBase
  ```

  ``` highlight
  extension PointData: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17PointDataAccessorC"></span>` `<span id="//apple_ref/swift/Class/PointDataAccessor" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk17PointDataAccessorC" class="token"><code>PointDataAccessor</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Point data accessor used for manipulating points that are part of a PointDataSource.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-pointdataaccessor" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class PointDataAccessor
  ```

  ``` highlight
  extension PointDataAccessor: NativeBase
  ```

  ``` highlight
  extension PointDataAccessor: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16PointDataBuilderC"></span>` `<span id="//apple_ref/swift/Class/PointDataBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk16PointDataBuilderC" class="token"><code>PointDataBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Builder of <a href="sdk-for-ios-navigate-maps#/s:7heresdk9PointDataC">`PointData`</a> instances.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-pointdatabuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class PointDataBuilder
  ```

  ``` highlight
  extension PointDataBuilder: NativeBase
  ```

  ``` highlight
  extension PointDataBuilder: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15PointDataSourceC"></span>` `<span id="//apple_ref/swift/Class/PointDataSource" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk15PointDataSourceC" class="token"><code>PointDataSource</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Point data source allows the rendering engine access to the user provided geographical locations and their attributes.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-pointdatasource" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class PointDataSource
  ```

  ``` highlight
  extension PointDataSource: NativeBase
  ```

  ``` highlight
  extension PointDataSource: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22PointDataSourceBuilderC"></span>` `<span id="//apple_ref/swift/Class/PointDataSourceBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk22PointDataSourceBuilderC" class="token"><code>PointDataSourceBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Builder of points data source.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-pointdatasourcebuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class PointDataSourceBuilder
  ```

  ``` highlight
  extension PointDataSourceBuilder: NativeBase
  ```

  ``` highlight
  extension PointDataSourceBuilder: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19PointTileDataSourceC"></span>` `<span id="//apple_ref/swift/Class/PointTileDataSource" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk19PointTileDataSourceC" class="token"><code>PointTileDataSource</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Point tile data source allows the rendering engine access to user managed data sets of geographical locations and their attributes through a <a href="sdk-for-ios-navigate-protocols-pointtilesource">`PointTileSource`</a>.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-pointtiledatasource" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class PointTileDataSource
  ```

  ``` highlight
  extension PointTileDataSource: NativeBase
  ```

  ``` highlight
  extension PointTileDataSource: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15PointTileSourceP"></span>` `<span id="//apple_ref/swift/Protocol/PointTileSource" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk15PointTileSourceP" class="token"><code>PointTileSource</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A source of geodetic point tiles. The implementations must be thread-safe.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-protocols-pointtilesource" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol PointTileSource : TileSource
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk32PointTileSourceLoadResultHandlerP"></span>` `<span id="//apple_ref/swift/Protocol/PointTileSourceLoadResultHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk32PointTileSourceLoadResultHandlerP" class="token"><code>PointTileSourceLoadResultHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Result handler of a load tile request.

  <a href="sdk-for-ios-navigate-protocols-pointtilesourceloadresulthandler" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol PointTileSourceLoadResultHandler : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15Point2DKeyframeV"></span>` `<span id="//apple_ref/swift/Struct/Point2DKeyframe" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk15Point2DKeyframeV" class="token"><code>Point2DKeyframe</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A Point2D keyframe. A keyframe consists of a value and an animation duration.

  <a href="sdk-for-ios-navigate-structs-point2dkeyframe" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Point2DKeyframe : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11PolygonDataC"></span>` `<span id="//apple_ref/swift/Class/PolygonData" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk11PolygonDataC" class="token"><code>PolygonData</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a geodetic polygon with custom attributes. Can be created using a <a href="sdk-for-ios-navigate-classes-polygondatabuilder">`PolygonDataBuilder`</a>.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class PolygonData
  ```

  ``` highlight
  extension PolygonData: NativeBase
  ```

  ``` highlight
  extension PolygonData: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19PolygonDataAccessorC"></span>` `<span id="//apple_ref/swift/Class/PolygonDataAccessor" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk19PolygonDataAccessorC" class="token"><code>PolygonDataAccessor</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Polygon data accessor used for manipulating polygons that are part of a PolygonDataSource.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-polygondataaccessor" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class PolygonDataAccessor
  ```

  ``` highlight
  extension PolygonDataAccessor: NativeBase
  ```

  ``` highlight
  extension PolygonDataAccessor: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18PolygonDataBuilderC"></span>` `<span id="//apple_ref/swift/Class/PolygonDataBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk18PolygonDataBuilderC" class="token"><code>PolygonDataBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Builder of <a href="sdk-for-ios-navigate-maps#/s:7heresdk11PolygonDataC">`PolygonData`</a> instances.

  The builder can create <a href="sdk-for-ios-navigate-maps#/s:7heresdk11PolygonDataC">`PolygonData`</a> instances for polygons with an outer boundary and optionally one or more inner boundaries (holes).

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-polygondatabuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class PolygonDataBuilder
  ```

  ``` highlight
  extension PolygonDataBuilder: NativeBase
  ```

  ``` highlight
  extension PolygonDataBuilder: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17PolygonDataSourceC"></span>` `<span id="//apple_ref/swift/Class/PolygonDataSource" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk17PolygonDataSourceC" class="token"><code>PolygonDataSource</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Polygon data source allows the rendering engine access to the user provided polygons geometry and their attributes.

  Polygon segments are rendered following the shortest path between their end points.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-polygondatasource" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class PolygonDataSource
  ```

  ``` highlight
  extension PolygonDataSource: NativeBase
  ```

  ``` highlight
  extension PolygonDataSource: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24PolygonDataSourceBuilderC"></span>` `<span id="//apple_ref/swift/Class/PolygonDataSourceBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk24PolygonDataSourceBuilderC" class="token"><code>PolygonDataSourceBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Builder of the polygons data source.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-polygondatasourcebuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class PolygonDataSourceBuilder
  ```

  ``` highlight
  extension PolygonDataSourceBuilder: NativeBase
  ```

  ``` highlight
  extension PolygonDataSourceBuilder: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21PolygonTileDataSourceC"></span>` `<span id="//apple_ref/swift/Class/PolygonTileDataSource" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk21PolygonTileDataSourceC" class="token"><code>PolygonTileDataSource</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Polygon tile data source allows the rendering engine access to user managed data sets of geodetic polygons and their attributes through a <a href="sdk-for-ios-navigate-protocols-polygontilesource">`PolygonTileSource`</a>.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-polygontiledatasource" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class PolygonTileDataSource
  ```

  ``` highlight
  extension PolygonTileDataSource: NativeBase
  ```

  ``` highlight
  extension PolygonTileDataSource: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17PolygonTileSourceP"></span>` `<span id="//apple_ref/swift/Protocol/PolygonTileSource" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk17PolygonTileSourceP" class="token"><code>PolygonTileSource</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A source of geodetic polygon tiles. Polygons provided by an implementation must be clipped to the boundaries of the requested tile. The implementations must be thread-safe.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-protocols-polygontilesource" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol PolygonTileSource : TileSource
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk34PolygonTileSourceLoadResultHandlerP"></span>` `<span id="//apple_ref/swift/Protocol/PolygonTileSourceLoadResultHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk34PolygonTileSourceLoadResultHandlerP" class="token"><code>PolygonTileSourceLoadResultHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Result handler of a load tile request.

  <a href="sdk-for-ios-navigate-protocols-polygontilesourceloadresulthandler" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol PolygonTileSourceLoadResultHandler : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15QuadMeshBuilderC"></span>` `<span id="//apple_ref/swift/Class/QuadMeshBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk15QuadMeshBuilderC" class="token"><code>QuadMeshBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Builder for a single quad.

  <a href="sdk-for-ios-navigate-classes-quadmeshbuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class QuadMeshBuilder : MeshBuilder
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16RasterDataSourceC"></span>` `<span id="//apple_ref/swift/Class/RasterDataSource" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk16RasterDataSourceC" class="token"><code>RasterDataSource</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Data source to load map layers using a raster image format (jpg, png). The example below illustrates how to create a raster data source and how to link it to a newly created map layer.

  ``` highlight
  let rasterDataSource = RasterDataSource ( mapContext , rasterDataSourceConfig ) let layer = MapLayerBuilder () // The name and the type of the data source have to be provided. // In our case, the name of the raster data source is in rasterDataSourceConfig. . withDataSource ( named : rasterDataSourceConfig . name , contentType : MapContentType . rasterImage ) . forMap ( map ) . withName ( "rasterLayer" ) . build ();
  ```

  </pre>

  <a href="sdk-for-ios-navigate-classes-rasterdatasource" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class RasterDataSource
  ```

  ``` highlight
  extension RasterDataSource: NativeBase
  ```

  ``` highlight
  extension RasterDataSource: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk29RasterDataSourceConfigurationV"></span>` `<span id="//apple_ref/swift/Struct/RasterDataSourceConfiguration" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk29RasterDataSourceConfigurationV" class="token"><code>RasterDataSourceConfiguration</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called on the main thread after

      fromJsonFile()

  method finishes loading the configuration.
  </p>

  <a href="sdk-for-ios-navigate-structs-rasterdatasourceconfiguration" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct RasterDataSourceConfiguration
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk35RasterDataSourceConfigurationUpdateV"></span>` `<span id="//apple_ref/swift/Struct/RasterDataSourceConfigurationUpdate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk35RasterDataSourceConfigurationUpdateV" class="token"><code>RasterDataSourceConfigurationUpdate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configuration update for a RasterDataSource.

  <a href="sdk-for-ios-navigate-structs-rasterdatasourceconfigurationupdate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct RasterDataSourceConfigurationUpdate
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24RasterDataSourceDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/RasterDataSourceDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk24RasterDataSourceDelegateP" class="token"><code>RasterDataSourceDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Delegate for RasterDataSource events.

  <a href="sdk-for-ios-navigate-protocols-rasterdatasourcedelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol RasterDataSourceDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21RasterDataSourceErrorO"></span>` `<span id="//apple_ref/swift/Enum/RasterDataSourceError" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk21RasterDataSourceErrorO" class="token"><code>RasterDataSourceError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Raster data source error codes.

  <a href="sdk-for-ios-navigate-enums-rasterdatasourceerror" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum RasterDataSourceError : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16RasterTileSourceP"></span>` `<span id="//apple_ref/swift/Protocol/RasterTileSource" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk16RasterTileSourceP" class="token"><code>RasterTileSource</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A source of raster tiles. The implementations must be thread-safe. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-protocols-rastertilesource" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol RasterTileSource : TileSource
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk33RasterTileSourceLoadResultHandlerP"></span>` `<span id="//apple_ref/swift/Protocol/RasterTileSourceLoadResultHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk33RasterTileSourceLoadResultHandlerP" class="token"><code>RasterTileSourceLoadResultHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Result handler of a load tile request.

  <a href="sdk-for-ios-navigate-protocols-rastertilesourceloadresulthandler" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol RasterTileSourceLoadResultHandler : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24RoadShieldIconPropertiesV"></span>` `<span id="//apple_ref/swift/Struct/RoadShieldIconProperties" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk24RoadShieldIconPropertiesV" class="token"><code>RoadShieldIconProperties</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contains the information required to create a road shield image.

  <a href="sdk-for-ios-navigate-structs-roadshieldiconproperties" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct RoadShieldIconProperties
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10RenderSizeV"></span>` `<span id="//apple_ref/swift/Struct/RenderSize" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk10RenderSizeV" class="token"><code>RenderSize</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents size of visual elements drawn on the map.

  <a href="sdk-for-ios-navigate-structs-rendersize" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct RenderSize
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14ScalarKeyframeV"></span>` `<span id="//apple_ref/swift/Struct/ScalarKeyframe" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk14ScalarKeyframeV" class="token"><code>ScalarKeyframe</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A ScalarKeyframe consists of a scalar value (e.g,: distance in meters) and an animation duration.

  <a href="sdk-for-ios-navigate-structs-scalarkeyframe" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ScalarKeyframe : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/c:@M@heresdk@objc(cs)SDKMapViewInitializer"></span>` `<span id="//apple_ref/swift/Class/SDKMapViewInitializer" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/c:@M@heresdk@objc(cs)SDKMapViewInitializer" class="token"><code>SDKMapViewInitializer</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Do not use this. This class is used to initialize internals of the SDK.

  <a href="sdk-for-ios-navigate-classes-sdkmapviewinitializer" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SDKMapViewInitializer : NSObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13ShadowQualityO"></span>` `<span id="//apple_ref/swift/Enum/ShadowQuality" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk13ShadowQualityO" class="token"><code>ShadowQuality</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The shadow quality. Controls the quality of the shadow cascade (i.e. the size of the shadow maps and the cascade count), which is shared by all views.

  <a href="sdk-for-ios-navigate-enums-shadowquality" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum ShadowQuality : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk5StyleC"></span>` `<span id="//apple_ref/swift/Class/Style" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk5StyleC" class="token"><code>Style</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A style that defines the visual appearance of map rendered features. A `Style` can be created using a <a href="sdk-for-ios-navigate-classes-jsonstylefactory">`JsonStyleFactory`</a>.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-style" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class Style
  ```

  ``` highlight
  extension Style: NativeBase
  ```

  ``` highlight
  extension Style: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11TapDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/TapDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk11TapDelegateP" class="token"><code>TapDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol for handling tap gestures. Tap gesture occurs after tapping on the screen.

  <a href="sdk-for-ios-navigate-protocols-tapdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol TapDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23TileGeoBoundsCalculatorC"></span>` `<span id="//apple_ref/swift/Class/TileGeoBoundsCalculator" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk23TileGeoBoundsCalculatorC" class="token"><code>TileGeoBoundsCalculator</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A calculator of geodetic bounds for tiles identified by keys generated in a particular tiling scheme (<a href="sdk-for-ios-navigate-enums-tilingscheme">`TilingScheme`</a>).

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-tilegeoboundscalculator" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class TileGeoBoundsCalculator
  ```

  ``` highlight
  extension TileGeoBoundsCalculator: NativeBase
  ```

  ``` highlight
  extension TileGeoBoundsCalculator: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10TileSourceP"></span>` `<span id="//apple_ref/swift/Protocol/TileSource" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk10TileSourceP" class="token"><code>TileSource</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A source of tiles. The implementations must be thread-safe.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-protocols-tilesource" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol TileSource : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21TileSourceDataVersionV"></span>` `<span id="//apple_ref/swift/Struct/TileSourceDataVersion" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk21TileSourceDataVersionV" class="token"><code>TileSourceDataVersion</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Tile data version.

  <a href="sdk-for-ios-navigate-structs-tilesourcedataversion" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TileSourceDataVersion
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18TileSourceDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/TileSourceDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk18TileSourceDelegateP" class="token"><code>TileSourceDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Delegate for <a href="sdk-for-ios-navigate-protocols-tilesource">`TileSource`</a> events.

  <a href="sdk-for-ios-navigate-protocols-tilesourcedelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol TileSourceDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk014TileSourceLoadB13RequestHandleP"></span>` `<span id="//apple_ref/swift/Protocol/TileSourceLoadTileRequestHandle" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk014TileSourceLoadB13RequestHandleP" class="token"><code>TileSourceLoadTileRequestHandle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Handle of a load request.

  <a href="sdk-for-ios-navigate-protocols-tilesourceloadtilerequesthandle" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol TileSourceLoadTileRequestHandle : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk010TileSourceB8MetadataV"></span>` `<span id="//apple_ref/swift/Struct/TileSourceTileMetadata" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk010TileSourceB8MetadataV" class="token"><code>TileSourceTileMetadata</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Tile metadata.

  <a href="sdk-for-ios-navigate-structs-tilesourcetilemetadata" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TileSourceTileMetadata
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7TileKeyV"></span>` `<span id="//apple_ref/swift/Struct/TileKey" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk7TileKeyV" class="token"><code>TileKey</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Key of a data source tile. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-tilekey" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TileKey : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22TileUrlProviderFactoryC"></span>` `<span id="//apple_ref/swift/Class/TileUrlProviderFactory" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk22TileUrlProviderFactoryC" class="token"><code>TileUrlProviderFactory</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Factory for generating a <a href="sdk-for-ios-navigate-maps#/s:7heresdk21TileUrlRequestHandlera">`TileUrlRequestHandler`</a> utilized in creating a tile URL.

  <a href="sdk-for-ios-navigate-classes-tileurlproviderfactory" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class TileUrlProviderFactory
  ```

  ``` highlight
  extension TileUrlProviderFactory: NativeBase
  ```

  ``` highlight
  extension TileUrlProviderFactory: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21TileUrlRequestHandlera"></span>` `<span id="//apple_ref/swift/Alias/TileUrlRequestHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk21TileUrlRequestHandlera" class="token"><code>TileUrlRequestHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Provides the URL as String for the given tile coordinates and storage level.

  The first and second parameters correspond to the X and Y coordinates of the tile, respectively, and have values ranging from 0 to 2^level − 1. The third parameter indicates the level of the tile.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias TileUrlRequestHandler = ( _ x : Int32 , _ y : Int32 , _ level : Int32 ) -> String
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
  <td><code> </code><em><code>x</code></em><code> </code></td>
  <td><div>
  <p>X coordinate of the tile. This ranges from 0 to 2^level − 1.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>y</code></em><code> </code></td>
  <td><div>
  <p>Y coordinate of the tile. This ranges from 0 to 2^level − 1.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>level</code></em><code> </code></td>
  <td><div>
  <p>Level of the tile.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  the URL.

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12TilingSchemeO"></span>` `<span id="//apple_ref/swift/Enum/TilingScheme" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk12TilingSchemeO" class="token"><code>TilingScheme</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of available data tiling schemes. X axis has the origin at -180 longitude and is increasing in east direction. Y axis has the origin at max latitude and is increasing in south direction. For half quad tree schemes, only the uppper half of the tree is used.

  <a href="sdk-for-ios-navigate-enums-tilingscheme" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TilingScheme : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24TranslucentMapLayerGroupC"></span>` `<span id="//apple_ref/swift/Class/TranslucentMapLayerGroup" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk24TranslucentMapLayerGroupC" class="token"><code>TranslucentMapLayerGroup</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A translucent layer group that can be the target for

      MapLayerPriorityBuilder.inGroup(...)

  . Currently, only custom line layers can be added to a translucent layer group. Custom line layers in a translucent layer group are rendered in an offscreen translucent pass so that overlapping translucent line geometry is not alpha blended with itself. At creation, the layer group gets added to a map. The layer group gets removed from the map upon instance destruction and any layer (categories) still in the group are not rendered anymore, therefore it is recommended to keep a group alive as long as layers using the group are alive and in use.
  </p>

  Conceptual example to place line layers into a translucent group:

  ``` highlight
  // Create a translucent group with a unique name and a render priority let groupPriority = MapLayerPriorityBuilder () . renderedLast () . build () let group = TranslucentMapLayerGroup ( name : "TranslucentGroupName" , map , groupPriority ) // Create a line layer to be rendered as part of the translucent group let lineLayerPriority = MapLayerPriorityBuilder () . inGroup ( "TranslucentGroupName" ) // places the line layer into the group . renderedFirst () // to be rendered first when the group is rendered . withCategory ( "SomeCategory" ) // places the line layer category 'SomeCategory' . inGroup ( "TranslucentGroupName" ) // into the group . renderedLast () // to be rendered last when the group is rendered . build () let lineLayer = MapLayerBuilder () . withDataSource ( named : "DataSourceName" , contentType : MapContentType . line ) . forMap ( map ) . withName ( "LineLayerName" ) . withPriority ( lineLayerPriority ) . withStyle ( translucentLineStyle ) // E.g. "technique": "line" ... "color": "#FFFFFF80" . build () // Create a second line layer to be rendered as part of the translucent group let secondLineLayerPriority = MapLayerPriorityBuilder () . inGroup ( "TranslucentGroupName" ) // places the second line layer into the group . renderedBeforeLayer ( "LineLayerName" ) // to be rendered before first layer // when the group is rendered . build () let secondLineLayer = MapLayerBuilder () . withDataSource ( named : "SecondDataSourceName" , contentType : MapContentType . line ) . forMap ( map ) . withName ( "SecondLineLayerName" ) . withPriority ( secondLineLayerPriority ) . withStyle ( secondTranslucentLineStyle ) // E.g. "technique": "line" ... "color": "#FFFFFF80" . build ()
  ```

  </pre>

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-translucentmaplayergroup" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class TranslucentMapLayerGroup
  ```

  ``` highlight
  extension TranslucentMapLayerGroup: NativeBase
  ```

  ``` highlight
  extension TranslucentMapLayerGroup: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19TriangleMeshBuilderC"></span>` `<span id="//apple_ref/swift/Class/TriangleMeshBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk19TriangleMeshBuilderC" class="token"><code>TriangleMeshBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Builder for a single triangle.

  <a href="sdk-for-ios-navigate-classes-trianglemeshbuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class TriangleMeshBuilder : MeshBuilder
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20TwoFingerPanDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/TwoFingerPanDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk20TwoFingerPanDelegateP" class="token"><code>TwoFingerPanDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol for handling two finger pan gestures. Two finger pan gesture occurs when two fingers are on the screen and both of them are moving vertically.

  <a href="sdk-for-ios-navigate-protocols-twofingerpandelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol TwoFingerPanDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20TwoFingerTapDelegateP"></span>` `<span id="//apple_ref/swift/Protocol/TwoFingerTapDelegate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk20TwoFingerTapDelegateP" class="token"><code>TwoFingerTapDelegate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol for handling two finger tap gestures. Two finger tap gesture occurs after tapping on the screen with two fingers.

  <a href="sdk-for-ios-navigate-protocols-twofingertapdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol TwoFingerTapDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15VisibilityStateO"></span>` `<span id="//apple_ref/swift/Enum/VisibilityState" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk15VisibilityStateO" class="token"><code>VisibilityState</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the visibility state of an SDK map view’s object.

  <a href="sdk-for-ios-navigate-enums-visibilitystate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum VisibilityState : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk32VehicleRestrictionIconPropertiesV"></span>` `<span id="//apple_ref/swift/Struct/VehicleRestrictionIconProperties" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk32VehicleRestrictionIconPropertiesV" class="token"><code>VehicleRestrictionIconProperties</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Encapsulates properties for generating vehicle restriction icons using <a href="sdk-for-ios-navigate-classes-iconprovider">`IconProvider`</a>.

  <a href="sdk-for-ios-navigate-structs-vehiclerestrictioniconproperties" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct VehicleRestrictionIconProperties
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14WatermarkStyleO"></span>` `<span id="//apple_ref/swift/Enum/WatermarkStyle" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-maps#/s:7heresdk14WatermarkStyleO" class="token"><code>WatermarkStyle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the style of the HERE watermark logo. The dark watermark should be used for custom schemes that are brighter (like daytime) and the light watermark for darker custom schemes (like night or satellite based).

  <a href="sdk-for-ios-navigate-enums-watermarkstyle" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum WatermarkStyle : UInt32, CaseIterable, Codable
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

