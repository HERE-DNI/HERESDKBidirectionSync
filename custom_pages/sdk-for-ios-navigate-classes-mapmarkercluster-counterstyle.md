---
title: "CounterStyle Structure Reference"
slug: "sdk-for-ios-navigate-classes-mapmarkercluster-counterstyle"
---

# CounterStyle

<div class="declaration">

<div class="language">

``` highlight
public struct CounterStyle
```

</div>

</div>

Styling options for a marker cluster which is represented by the marker count as a text.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk16MapMarkerClusterC12CounterStyleV9textColorSo7UIColorCvp"></span>` `<span id="//apple_ref/swift/Property/textColor" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mapmarkercluster-counterstyle#/s:7heresdk16MapMarkerClusterC12CounterStyleV9textColorSo7UIColorCvp" class="token"><code>textColor</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Font color of counter. Default value is white.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var textColor: UIColor
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16MapMarkerClusterC12CounterStyleV8fontSizeSdvp"></span>` `<span id="//apple_ref/swift/Property/fontSize" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mapmarkercluster-counterstyle#/s:7heresdk16MapMarkerClusterC12CounterStyleV8fontSizeSdvp" class="token"><code>fontSize</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Font size of counter. Default value is 20.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var fontSize: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16MapMarkerClusterC12CounterStyleV10textAnchorAA8Anchor2DVvp"></span>` `<span id="//apple_ref/swift/Property/textAnchor" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mapmarkercluster-counterstyle#/s:7heresdk16MapMarkerClusterC12CounterStyleV10textAnchorAA8Anchor2DVvp" class="token"><code>textAnchor</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Anchor of counter in regards to marker cluster image. Default is at the center.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var textAnchor: Anchor2D
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16MapMarkerClusterC12CounterStyleV14maxCountNumbers5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/maxCountNumber" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mapmarkercluster-counterstyle#/s:7heresdk16MapMarkerClusterC12CounterStyleV14maxCountNumbers5Int32Vvp" class="token"><code>maxCountNumber</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Maximal number of markers represented as exact number. Values smaller than 2 will be clamped to 2. Default value is 99. When this value is changed, it is recommended to adapt <a href="sdk-for-ios-navigate-classes-mapmarkercluster-counterstyle#/s:7heresdk16MapMarkerClusterC12CounterStyleV12aboveMaxTextSSvp">`MapMarkerCluster.CounterStyle.aboveMaxText`</a> accordingly.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxCountNumber: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16MapMarkerClusterC12CounterStyleV12aboveMaxTextSSvp"></span>` `<span id="//apple_ref/swift/Property/aboveMaxText" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mapmarkercluster-counterstyle#/s:7heresdk16MapMarkerClusterC12CounterStyleV12aboveMaxTextSSvp" class="token"><code>aboveMaxText</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  String to display if there are more markers clustered than <a href="sdk-for-ios-navigate-classes-mapmarkercluster-counterstyle#/s:7heresdk16MapMarkerClusterC12CounterStyleV14maxCountNumbers5Int32Vvp">`MapMarkerCluster.CounterStyle.maxCountNumber`</a>. Default value is “+99”.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var aboveMaxText: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(textColor: fontSize: textAnchor: maxCountNumber: aboveMaxText: )

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
  public init ( textColor : UIColor = NamedColor . white , fontSize : Double = 20.0 , textAnchor : Anchor2D = Anchor2D (), maxCountNumber : Int32 = 99 , aboveMaxText : String = "+99" )
  ```

  </pre>

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

