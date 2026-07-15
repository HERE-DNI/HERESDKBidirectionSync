---
title: "TransitTransport Structure Reference"
slug: "sdk-for-ios-explore-structs-transittransport"
---

# TransitTransport

<div class="declaration">

<div class="language">

``` highlight
public struct TransitTransport : Hashable
```

</div>

</div>

Holds all the transit transport information.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk16TransitTransportV4modeAA0B4ModeOvp"></span>` `<span id="//apple_ref/swift/Property/mode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-transittransport#/s:7heresdk16TransitTransportV4modeAA0B4ModeOvp" class="token"><code>mode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Transit mode of transport in the route.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var mode: TransitMode
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16TransitTransportV4nameSSSgvp"></span>` `<span id="//apple_ref/swift/Property/name" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-transittransport#/s:7heresdk16TransitTransportV4nameSSSgvp" class="token"><code>name</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Transit line name.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var name: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16TransitTransportV8headsignSSSgvp"></span>` `<span id="//apple_ref/swift/Property/headsign" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-transittransport#/s:7heresdk16TransitTransportV8headsignSSSgvp" class="token"><code>headsign</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Transit line headsign.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var headsign: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16TransitTransportV8categorySSSgvp"></span>` `<span id="//apple_ref/swift/Property/category" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-transittransport#/s:7heresdk16TransitTransportV8categorySSSgvp" class="token"><code>category</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Human readable transport category (such as Bus, Gondola, Tram, Train, …)

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var category: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16TransitTransportV5colorSo7UIColorCSgvp"></span>` `<span id="//apple_ref/swift/Property/color" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-transittransport#/s:7heresdk16TransitTransportV5colorSo7UIColorCSgvp" class="token"><code>color</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Color of the transport polyline and background for the transport name.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var color: UIColor?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16TransitTransportV9textColorSo7UIColorCSgvp"></span>` `<span id="//apple_ref/swift/Property/textColor" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-transittransport#/s:7heresdk16TransitTransportV9textColorSo7UIColorCSgvp" class="token"><code>textColor</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Color of the transport name.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var textColor: UIColor?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(mode: name: headsign: category: color: textColor: )

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
  public init ( mode : TransitMode , name : String ? = nil , headsign : String ? = nil , category : String ? = nil , color : UIColor ? = nil , textColor : UIColor ? = nil )
  ```

  </pre>

  </div>

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

