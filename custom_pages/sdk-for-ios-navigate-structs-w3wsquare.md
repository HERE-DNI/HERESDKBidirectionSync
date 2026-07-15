---
title: "W3WSquare Structure Reference"
slug: "sdk-for-ios-navigate-structs-w3wsquare"
---

# W3WSquare

<div class="declaration">

<div class="language">

``` highlight
public struct W3WSquare : Hashable
```

</div>

</div>

Contains information about one of the squares in the what3words geocode system.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk9W3WSquareV6squareAA6GeoBoxVvp"></span>` `<span id="//apple_ref/swift/Property/square" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-w3wsquare#/s:7heresdk9W3WSquareV6squareAA6GeoBoxVvp" class="token"><code>square</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A 3-by-3-metre square defined by the what3words geocode system.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var square: GeoBox
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9W3WSquareV11coordinatesAA14GeoCoordinatesVvp"></span>` `<span id="//apple_ref/swift/Property/coordinates" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-w3wsquare#/s:7heresdk9W3WSquareV11coordinatesAA14GeoCoordinatesVvp" class="token"><code>coordinates</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The center of the square.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var coordinates: GeoCoordinates
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9W3WSquareV5wordsSSvp"></span>` `<span id="//apple_ref/swift/Property/words" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-w3wsquare#/s:7heresdk9W3WSquareV5wordsSSvp" class="token"><code>words</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  3 word address of the square, for example “///wage.mere.heap”.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var words: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9W3WSquareV12languageCodeSSvp"></span>` `<span id="//apple_ref/swift/Property/languageCode" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-w3wsquare#/s:7heresdk9W3WSquareV12languageCodeSSvp" class="token"><code>languageCode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The language code of the words as an ISO 639-1 2 letter code. Each supported language has its own set of words for each of the squares in the what3words geocode system. For Bosnian-Croatian-Montenegrin-Serbian, a special code “oo” is used.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var languageCode: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9W3WSquareV11countryCodeSSSgvp"></span>` `<span id="//apple_ref/swift/Property/countryCode" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-w3wsquare#/s:7heresdk9W3WSquareV11countryCodeSSSgvp" class="token"><code>countryCode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Country that contains the square. Not set if the square is in an area not governed by a specific country, such as international waters, Antarctica, some uninhabited islands etc.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var countryCode: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(square: coordinates: words: languageCode: countryCode: )

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
  public init ( square : GeoBox , coordinates : GeoCoordinates , words : String , languageCode : String , countryCode : String ? = nil )
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

