---
title: "MapView Class Reference"
slug: "sdk-for-ios-navigate-classes-mapview"
---

# MapView

<div class="declaration">

<div class="language">

``` highlight
@IBDesignable
@objc(HereMapView)
@MainActor
open class MapView : UIView, MapViewBase
```

</div>

Related types:

- <a href="sdk-for-ios-navigate-protocols-mapviewbase">MapViewBase</a>

</div>

A view that displays a map. Note: Before using this class, <a href="sdk-for-ios-navigate-classes-sdknativeengine">`SDKNativeEngine`</a> must be already initialized.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC22TakeScreenshotCallbacka"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-TakeScreenshotCallback" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC22TakeScreenshotCallbacka" class="token"><code>TakeScreenshotCallback</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Callback to be called on retrieval of screenshot.

  <div class="aside aside-note">

  Note

  In case of any error passed result is null.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias TakeScreenshotCallback = (UIImage?) -> Void
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC0C3PinC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-ViewPin" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC0C3PinC" class="token"><code>ViewPin</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class represents a pinned UIView, that means an UIView at a fixed location on the map.

  The pinned view will automatically be repositioned on the screen as the map moves. There is more performance overhead involved in positioning an view as compared to a map marker, so for use cases which only require static images, markers should be used.

  <a href="sdk-for-ios-navigate-classes-mapview-viewpin" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class ViewPin
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC6cameraAA0B6CameraCvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-camera" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC6cameraAA0B6CameraCvp" class="token"><code>camera</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The MapCamera to control the angle of view for the map

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public var camera: MapCamera { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapcamera">MapCamera</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC8gesturesAA8GesturesCvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-gestures" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC8gesturesAA8GesturesCvp" class="token"><code>gestures</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The gestures control object for setting up the capture of gestures.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public var gestures: Gestures { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-gestures">Gestures</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapViewBaseP8mapSceneAA0bF0Cvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-mapScene" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk11MapViewBaseP8mapSceneAA0bF0Cvp" class="token"><code>mapScene</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public var mapScene: MapScene { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapscene">MapScene</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapViewBaseP10mapContextAA0bF0Cvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-mapContext" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk11MapViewBaseP10mapContextAA0bF0Cvp" class="token"><code>mapContext</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public var mapContext: MapContext { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapcontext">MapContext</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapViewBaseP04hereB0AA04HereB0Cvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-hereMap" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk11MapViewBaseP04hereB0AA04HereB0Cvp" class="token"><code>hereMap</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public var hereMap: HereMap { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-heremap">HereMap</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC9frameRates5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-frameRate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC9frameRates5Int32Vvp" class="token"><code>frameRate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Maximum render frame rate in frames per second. Setting to 0 disables automatic rendering for this view. Setting negative values has no effect. The default value is 60 frames per second.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public var frameRate: Int32 { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC12viewportSizeAA6Size2DVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-viewportSize" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC12viewportSizeAA6Size2DVvp" class="token"><code>viewportSize</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns the viewport size in physical pixels.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public var viewportSize: Size2D { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-size2d">Size2D</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC15primaryLanguageAA0E4CodeOSgvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-primaryLanguage" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC15primaryLanguageAA0E4CodeOSgvpZ" class="token"><code>primaryLanguage</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The code of the desired primary map display language. If not set or if the desired language is not supported, then the language of the displayed region is used, which is the default behaviour. Applies to all instances of MapView. When changed, triggers redraw of any visible MapView.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public static var primaryLanguage: LanguageCode? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-languagecode">LanguageCode</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC17secondaryLanguageAA0E4CodeOSgvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-secondaryLanguage" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC17secondaryLanguageAA0E4CodeOSgvpZ" class="token"><code>secondaryLanguage</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The code of the desired secondary map display language. If the desired language is not supported, then the language of the displayed region is used. If not set, no secondary map language will be used which is the default behaviour. Applies to all instances of MapView. When changed, triggers redraw of any visible MapView. Note: This feature is in beta state and thus there can be bugs and unexpected behavior.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public static var secondaryLanguage: LanguageCode? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-languagecode">LanguageCode</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC13shadowQualityAA06ShadowE0OvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-shadowQuality" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC13shadowQualityAA06ShadowE0OvpZ" class="token"><code>shadowQuality</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The shadow quality for all instances of MapView. The quality controls the size of the shadow maps and the cascade count. The default shadow quality is {@code ShadowQuality.medium}. MapViews can request to render shadows by feature. Enabling shadows has a performance impact and should be considered only for devices with sufficient performance. Note: This feature is in beta state and thus there can be bugs and unexpected behavior.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public static var shadowQuality: ShadowQuality { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-shadowquality">ShadowQuality</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC5pauseyyF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-pause" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC5pauseyyF" class="token"><code>pause()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Pauses rendering of this instance of map view.

  Normally the application doesn’t need to call this method since the required handling of foreground/background switch is done from inside the HERESDK. However, if this needs to be called for some special reasons on application side, the application must call this method in

      applicationWillResignActive(_:)

  of the application delegate or
      sceneWillResignActive(_:)

  of the scene delegate. Otherwise, it may result in rendering glitches as the renderer is prohibited from issuing rendering commands when being in background.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public func pause()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC6resumeyyF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-resume" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC6resumeyyF" class="token"><code>resume()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Resumes rendering of this instance of map view.

  Normally the application doesn’t need to call this method since the required handling of foreground/background switch is done from inside the HERESDK. However, if this needs to be called for some special reasons on application side, the application must call this method in

      applicationDidBecomeActive(_:)

  of the application delegate or
      sceneDidBecomeActive(_:)

  of the scene delegate.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public func resume()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-c-M-heresdk-objc-csHereMapView-iminit"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-c-M-heresdk-objc-csHereMapView-iminit" class="token"><code>init()</code></a> 

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
  @MainActor
  public convenience init()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-c-M-heresdk-objc-csHereMapView-iminitWithFrame"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-frame" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-c-M-heresdk-objc-csHereMapView-iminitWithFrame" class="token"><code>init(frame:</code><wbr></wbr><code>)</code></a> 

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
  @MainActor
  override public convenience init(frame: CGRect)
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC7optionsAcA0bC7OptionsV_tcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-options" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC7optionsAcA0bC7OptionsV_tcfc" class="token"><code>init(options:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Initializes and returns a newly allocated view object

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public convenience init(options: MapViewOptions)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-mapviewoptions">MapViewOptions</a>

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
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>Customization of view for example its map projection</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC5frame7optionsACSo6CGRectV_AA0bC7OptionsVtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-frame-options" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC5frame7optionsACSo6CGRectV_AA0bC7OptionsVtcfc" class="token"><code>init(frame:</code><wbr></wbr><code>options:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Initializes and returns a newly allocated view object with the specified frame rectangle.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public convenience init(frame: CGRect, options: MapViewOptions)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-mapviewoptions">MapViewOptions</a>

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
  <td><code> </code><em><code>frame</code></em><code> </code></td>
  <td><div>
  <p>The frame rectangle for the view, measured in points.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>Customization of view for example its map projection</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC5frame13withSdkEngine7optionsACSo6CGRectV_AA09SDKNativeG0CAA0bC7OptionsVtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-frame-withSdkEngine-options" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC5frame13withSdkEngine7optionsACSo6CGRectV_AA09SDKNativeG0CAA0bC7OptionsVtcfc" class="token"><code>init(frame:</code><wbr></wbr><code>withSdkEngine:</code><wbr></wbr><code>options:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Initializes and returns a newly allocated view object with the specified frame rectangle and sdk engine.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public convenience init(frame: CGRect, withSdkEngine sdkEngine: SDKNativeEngine, options: MapViewOptions)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-sdknativeengine">SDKNativeEngine</a>
  - <a href="sdk-for-ios-navigate-structs-mapviewoptions">MapViewOptions</a>

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
  <td><code> </code><em><code>frame</code></em><code> </code></td>
  <td><div>
  <p>The frame rectangle for the view, measured in points.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>withSdkEngine</code></em><code> </code></td>
  <td><div>
  <p>object used previously to initialize whole sdk</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>options</code></em><code> </code></td>
  <td><div>
  <p>Optional customization of view for example its map projection</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC5frame13withSdkEngineACSo6CGRectV_AA09SDKNativeG0Ctcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-frame-withSdkEngine" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC5frame13withSdkEngineACSo6CGRectV_AA09SDKNativeG0Ctcfc" class="token"><code>init(frame:</code><wbr></wbr><code>withSdkEngine:</code><wbr></wbr><code>)</code></a> 

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
  @MainActor
  public convenience init(frame: CGRect, withSdkEngine sdkEngine: SDKNativeEngine)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-sdknativeengine">SDKNativeEngine</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC5frame13withSdkEngine0E7OptionsACSo6CGRectV_AA09SDKNativeG0CAA0bcH0VSgtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-frame-withSdkEngine-withOptions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC5frame13withSdkEngine0E7OptionsACSo6CGRectV_AA09SDKNativeG0CAA0bcH0VSgtcfc" class="token"><code>init(frame:</code><wbr></wbr><code>withSdkEngine:</code><wbr></wbr><code>withOptions:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Initializes and returns a newly allocated view object with specified frame rectangle, sdk engine and options.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public init(frame: CGRect, withSdkEngine sdkEngine: SDKNativeEngine, withOptions options: MapViewOptions?)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-sdknativeengine">SDKNativeEngine</a>
  - <a href="sdk-for-ios-navigate-structs-mapviewoptions">MapViewOptions</a>

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
  <td><code> </code><em><code>frame</code></em><code> </code></td>
  <td><div>
  <p>The frame rectangle for the view, measured in points.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>withSdkEngine</code></em><code> </code></td>
  <td><div>
  <p>Object that was previously used to initialize whole sdk.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>withOptions</code></em><code> </code></td>
  <td><div>
  <p>Optional customization of view for example its map projection.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-c-M-heresdk-objc-csHereMapView-iminitWithCoder"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-coder" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-c-M-heresdk-objc-csHereMapView-iminitWithCoder" class="token"><code>init(coder:</code><wbr></wbr><code>)</code></a> 

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
  @MainActor
  public required init?(coder aDecoder: NSCoder)
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC7isValidSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-isValid" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC7isValidSbvp" class="token"><code>isValid</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates whether this instance is valid. It will be made invalid when the corresponding <a href="sdk-for-ios-navigate-classes-sdknativeengine">`SDKNativeEngine`</a> is destroyed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public var isValid: Bool { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC05geoToC11Coordinates0dF0AA7Point2DVSgAA03GeoF0V_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-geoToViewCoordinates-geoCoordinates" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC05geoToC11Coordinates0dF0AA7Point2DVSgAA03GeoF0V_tF" class="token"><code>geoToViewCoordinates(geoCoordinates:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Converts geographical coordinates to view coordinates (in pixels).

  If specified, altitude of the input coordinates is interpreted as altitude above sea level. If not specified, the input coordinates are interpreted as being on ground elevation. The above distinction is only relevant when 3D terrain feature is enabled.

  The resulting view coordinates might be outside of current viewport, i.e. result might contain values less than zero or greater than view’s dimensions.

  If the render surface is not attached, it will return `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public func geoToViewCoordinates(geoCoordinates: GeoCoordinates) -> Point2D?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a>
  - <a href="sdk-for-ios-navigate-structs-point2d">Point2D</a>

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
  <td><code> </code><em><code>geoCoordinates</code></em><code> </code></td>
  <td><div>
  <p>Geographical coordinates to convert.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The view coordinates of the specified geographical point or `nil` if there is no render surface attached.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC20viewToGeoCoordinates0dG0AA0fG0VSgAA7Point2DV_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-viewToGeoCoordinates-viewCoordinates" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC20viewToGeoCoordinates0dG0AA0fG0VSgAA7Point2DV_tF" class="token"><code>viewToGeoCoordinates(viewCoordinates:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Converts view coordinates to geographical coordinates.

  An optional altitude component of the resulting geographical coordinate is not set.

  If the view coordinates specify a point above a horizon, then the result is geographical coordinates of the point on a horizon below the specified view coordinates.

  The fog effect is ignored for the calculation, meaning that for the view point within the area covered by the fog, the result is geographical coordinates that would be displayed at the specified point if the fog effect was not applied.

  If the render surface is not attached, it will return `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public func viewToGeoCoordinates(viewCoordinates: Point2D) -> GeoCoordinates?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-point2d">Point2D</a>
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
  <td><code> </code><em><code>viewCoordinates</code></em><code> </code></td>
  <td><div>
  <p>Point inside the view to convert.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The geographical coordinates under specified view point or `nil` if there is no render surface attached.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC4pick6filter6inside10completionyAA0B5SceneC0B10PickFilterCSg_AA11Rectangle2DVyAA0bI6ResultCSgctF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-pick-filter-inside-completion" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC4pick6filter6inside10completionyAA0B5SceneC0B10PickFilterCSg_AA11Rectangle2DVyAA0bI6ResultCSgctF" class="token"><code>pick(filter:</code><wbr></wbr><code>inside:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns all map content located inside the specified pick area. Content to be picked is specified by a pick content filter. The pick area is defined by a rectangle in map view coordinates in pixels, relative to the map view’s origin at (0, 0) which indicates the top-left corner of the map view.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public func pick(filter: MapScene.MapPickFilter?, inside viewArea: Rectangle2D, completion callback: @escaping (MapPickResult?) -> Void)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapscene">MapScene</a>
  - <a href="sdk-for-ios-navigate-structs-rectangle2d">Rectangle2D</a>
  - <a href="sdk-for-ios-navigate-classes-mappickresult">MapPickResult</a>

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
  <td><code> </code><em><code>filter</code></em><code> </code></td>
  <td><div>
  <p>Filter for the map content to be picked. When a filter is not set all of the pickable content will be picked.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>viewArea</code></em><code> </code></td>
  <td><div>
  <p>The rectangular pixel area of the view inside which map content will be picked. View area is relative to the map view’s origin at (0, 0) at the top-left corner of the map view.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>callback</code></em><code> </code></td>
  <td><div>
  <p>Callback to call with the result. This will be called on a main thread when pick operation completes.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC14takeScreenshot8callbackyySo7UIImageCSgc_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-takeScreenshot-callback" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC14takeScreenshot8callbackyySo7UIImageCSgc_tF" class="token"><code>takeScreenshot(callback:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously retrieves a screenshot of current map view. Note that this does not work when the map view is currently not visible, for example, when an application is running in background - even if MapView.pause() was not called.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public func takeScreenshot(callback: @escaping TakeScreenshotCallback)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC22TakeScreenshotCallbacka">TakeScreenshotCallback</a>

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
  <td><code> </code><em><code>callback</code></em><code> </code></td>
  <td><div>
  <p>Completion handler called when the screenshot is completed.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC20addLifecycleDelegateyyAA0bceF0_pF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-addLifecycleDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC20addLifecycleDelegateyyAA0bceF0_pF" class="token"><code>addLifecycleDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a <a href="sdk-for-ios-navigate-protocols-mapviewlifecycledelegate">`MapViewLifecycleDelegate`</a> to this map view. Adding the same object multiple times has no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public func addLifecycleDelegate(_ lifecycleListener: MapViewLifecycleDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-protocols-mapviewlifecycledelegate">MapViewLifecycleDelegate</a>

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
  <td><code> </code><em><code>lifecycleListener</code></em><code> </code></td>
  <td><div>
  <p>An object to be notified of lifecycle events.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC23removeLifecycleDelegateyyAA0bceF0_pF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-removeLifecycleDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC23removeLifecycleDelegateyyAA0bceF0_pF" class="token"><code>removeLifecycleDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a <a href="sdk-for-ios-navigate-protocols-mapviewlifecycledelegate">`MapViewLifecycleDelegate`</a> from this map view. Trying to remove an object that was not added or was removed before has no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public func removeLifecycleDelegate(_ lifecycleListener: MapViewLifecycleDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-protocols-mapviewlifecycledelegate">MapViewLifecycleDelegate</a>

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
  <td><code> </code><em><code>lifecycleListener</code></em><code> </code></td>
  <td><div>
  <p>An object to stop being notified of lifecycle events.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC6reinityyF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-reinit" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC6reinityyF" class="token"><code>reinit()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Reinitializes the map renderer. Does nothing if <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC7isValidSbvp">`isValid`</a> is `true` or <a href="sdk-for-ios-navigate-classes-sdknativeengine#sdk-for-ios-navigate-s-7heresdk15SDKNativeEngineC14sharedInstanceACSgvpZ">`SDKNativeEngine.sharedInstance`</a> is `nil`.

  This can be used after `MapView` gets invalidated as a result of destroying the shared <a href="sdk-for-ios-navigate-classes-sdknativeengine">`SDKNativeEngine`</a> and setting a new shared <a href="sdk-for-ios-navigate-classes-sdknativeengine">`SDKNativeEngine`</a>.

  After this call finishes successfully, <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC7isValidSbvp">`isValid`</a> becomes `true`.

  Map state is not preserved. The caller must load a scene, set camera, re-add all the delegates and all the map items, etc.

  Any previously stored instances of <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC6cameraAA0B6CameraCvp">`MapView.camera`</a>, <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk11MapViewBaseP8mapSceneAA0bF0Cvp">`MapView.mapScene`</a>, <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk11MapViewBaseP10mapContextAA0bF0Cvp">`MapView.mapContext`</a>, <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC8gesturesAA8GesturesCvp">`MapView.gestures`</a> and <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk11MapViewBaseP04hereB0AA04HereB0Cvp">`MapView.hereMap`</a> remain invalid.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public func reinit()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC20setWatermarkLocation6anchor6offsetyAA8Anchor2DV_AA7Point2DVtF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-setWatermarkLocation-anchor-offset" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC20setWatermarkLocation6anchor6offsetyAA8Anchor2DV_AA7Point2DVtF" class="token"><code>setWatermarkLocation(anchor:</code><wbr></wbr><code>offset:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the position of the HERE logo watermark within the map view.

  By default, the watermark is aligned to the bottom-right corner of the view: Anchor2D(1.0, 1.0) and Point2D(-watermarkSize.width / 2, -watermarkSize.height / 2). It is recommended to change the default position only if necessary to avoid overlapping UI elements. The watermark should always be fully visible within the view. The anchor point on the watermark is its center (width/2, height/2), around which it will be placed in the map view. For map views smaller than 250 dip in both width and height, the watermark will not be shown.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public func setWatermarkLocation(anchor: Anchor2D, offset: Point2D)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-anchor2d">Anchor2D</a>
  - <a href="sdk-for-ios-navigate-structs-point2d">Point2D</a>

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
  <td><code> </code><em><code>anchor</code></em><code> </code></td>
  <td><div>
  <p>Anchor point in normalized view coordinates [0, 1]. Map view’s origin at (0, 0) indicates a top-left corner of the map view. Out of boundary anchor point values will be clamped to the [0, 1] range.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>offset</code></em><code> </code></td>
  <td><div>
  <p>A horizontal and vertical offset (expressed in positive/negative pixel coordinates) that allows shifting the watermark from the anchor point position in one or the other direction. For the quadrant of values expressing visible part of the map view negative offset shifts the watermark to the direction of the origin, positive - away from it. For example, the offset of (-10, 5) will shift the watermark 10px to the left and 5px to the bottom. If specified offset will result in watermark being completely or partially out-of-view the offset will be adjusted internally so that watermark is fully visible. Offset is not being scaled when the map view size changes.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC10pixelScaleSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-pixelScale" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC10pixelScaleSdvp" class="token"><code>pixelScale</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The pixel scale factor used by this MapView. It is used to support screen resolution and size independence. This value is a derivative of the device’s screen pixel density and is a direct analog of the native scale factor for the physical screen.

  It can be used to translate between physical pixels and points according to formula: points = pixels / pixel_scale.

  Pixel scale is 0.0 if the map view is not initialized.

  In cases where the MapView moves in between screens (e.g. from main screen to a CarPlay screen), the most up-to-date pixel scale value can be obtained after a render target gets attached to the view. To get notified when a render target gets attached to the MapView, see `MapViewLifecycleDelegate.onAttach`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public var pixelScale: Double { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC13watermarkSizeAA6Size2DVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-watermarkSize" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC13watermarkSizeAA6Size2DVvp" class="token"><code>watermarkSize</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Provides the size of the watermark in physical pixels.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public var watermarkSize: Size2D { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-size2d">Size2D</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC03pinC0_2toAC0C3PinCSgSo6UIViewC_AA14GeoCoordinatesVtF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-pinView-_-to" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC03pinC0_2toAC0C3PinCSgSo6UIViewC_AA14GeoCoordinatesVtF" class="token"><code>pinView(_:</code><wbr></wbr><code>to:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Pins a `UIView` to the `MapView` and returns a proxy object that can be used to control the pinning. Trying to pin a view that was already pinned or a view that has a super view has no effect and returns `nil`.

  The altitude component of the coordinates, if set, is interpreted as above sea level. When not set, the coordinates are interpreted as at ground level.

  Please note, a pinned `UIView` will be confined to the bounds of `MapView` by default. If this is not desired, setting `MapView`‘s property `clipsToBounds` to false will allow pinned views to exceed `MapView`’s bounds.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public func pinView(_ view: UIView, to coordinates: GeoCoordinates) -> ViewPin?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a>
  - <a href="sdk-for-ios-navigate-classes-mapview-viewpin">ViewPin</a>

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
  <td><code> </code><em><code>view</code></em><code> </code></td>
  <td><div>
  <p><code>UIView</code> object to pin.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>coordinates</code></em><code> </code></td>
  <td><div>
  <p><a href="sdk-for-ios-navigate-structs-geocoordinates"><code>GeoCoordinates</code></a> to pin the view at.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The <a href="sdk-for-ios-navigate-classes-mapview-viewpin">`ViewPin`</a> proxy object, or `nil` if view was not pinned.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC05unpinC0yySo6UIViewCF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-unpinView-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC05unpinC0yySo6UIViewCF" class="token"><code>unpinView(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a ViewPin from the MapView by specifying the corresponding UIView. Trying to unpin a view that was not pinned or was unpinned before has no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public func unpinView(_ view: UIView)
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
  <td><code> </code><em><code>view</code></em><code> </code></td>
  <td><div>
  <p>The UIView corresponding to the ViewPin to remove.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC8viewPinsSayAC0C3PinCGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-viewPins" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC8viewPinsSayAC0C3PinCGvp" class="token"><code>viewPins</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets a copy of the array of currently added view pins.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public var viewPins: [MapView.ViewPin] { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapview-viewpin">ViewPin</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7MapViewC15handleLowMemoryyyF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-handleLowMemory" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapview#sdk-for-ios-navigate-s-7heresdk7MapViewC15handleLowMemoryyyF" class="token"><code>handleLowMemory()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Handles low memory situation.

  This method should be called from a view controller, when it receives a memory warning (

      UIViewController.didReceiveMemoryWarning()

  )
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @MainActor
  public func handleLowMemory()
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

