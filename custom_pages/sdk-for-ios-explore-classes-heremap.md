---
title: "HereMap Class Reference"
slug: "sdk-for-ios-explore-classes-heremap"
---

# HereMap

<div class="declaration">

<div class="language">

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

The representation of a dynamic and interactive geographic map. The map manages a collection of layers of objects and spaces, presents them in a stacked layout and offers the means to focus on a certain area. The layers, their relation to the objects and spaces, the layout and the representation style is described through a configuration.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk7HereMapC5styleAA5StyleCvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-style" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-heremap#sdk-for-ios-explore-s-7heresdk7HereMapC5styleAA5StyleCvp" class="token"><code>style</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The style that the map uses to customize the visual appearance of rendered features. Changes made to the map style using <a href="sdk-for-ios-explore-classes-style#sdk-for-ios-explore-s-7heresdk5StyleC6updateyyACF">`Style.update(...)`</a> are lost when new scene is loaded using

      MapScene.loadScene(MapScheme, MapScene.LoadSceneCompletionHandler?)

  and its variants as well as when map features are enabled or disabled using <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">`MapScene.enableFeatures(...)`</a> and <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC15disableFeaturesyySaySSGF">`MapScene.disableFeatures(...)`</a>.
  </p>

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var style: Style { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-style">Style</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk7HereMapC03addC12IdleDelegateyyAA0ceF0_pF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addMapIdleDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-heremap#sdk-for-ios-explore-s-7heresdk7HereMapC03addC12IdleDelegateyyAA0ceF0_pF" class="token"><code>addMapIdleDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a delegate for receiving idle state notifications and notifies it of the current state.

  The first notification received is always the state at the time of registration.

  The new delegate is appended to the set of `HereMap` idle delegates as a strong reference. The caller is responsible for releasing the strong reference by calling <a href="sdk-for-ios-explore-classes-heremap#sdk-for-ios-explore-s-7heresdk7HereMapC06removeC12IdleDelegateyyAA0ceF0_pF">`HereMap.removeMapIdleDelegate(...)`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addMapIdleDelegate(_ delegate: MapIdleDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-mapidledelegate">MapIdleDelegate</a>

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
  <p>The delegate</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk7HereMapC06removeC12IdleDelegateyyAA0ceF0_pF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeMapIdleDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-heremap#sdk-for-ios-explore-s-7heresdk7HereMapC06removeC12IdleDelegateyyAA0ceF0_pF" class="token"><code>removeMapIdleDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a delegate from receiving idle state notifications.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeMapIdleDelegate(_ delegate: MapIdleDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-mapidledelegate">MapIdleDelegate</a>

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
  <p>The delegate</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

