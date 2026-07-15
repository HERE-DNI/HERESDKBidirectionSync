---
title: "Suggestion Class Reference"
slug: "sdk-for-ios-navigate-classes-suggestion"
---

# Suggestion

<div class="declaration">

<div class="language">

``` highlight
public class Suggestion
```

``` highlight
extension Suggestion: NativeBase
```

``` highlight
extension Suggestion: Hashable
```

</div>

</div>

Suggestion is meant to provide relevant suggestions to partial queries, like “restaur”, “starbu”, “eiffel”. Represents a relevant response to user queries. Suggestions (please check <a href="sdk-for-ios-navigate-enums-suggestiontype">`SuggestionType`</a>) are either: Place: <a href="sdk-for-ios-navigate-enums-suggestiontype#/s:7heresdk14SuggestionTypeO5placeyA2CmF">`SuggestionType.place`</a> Query: <a href="sdk-for-ios-navigate-enums-suggestiontype#/s:7heresdk14SuggestionTypeO5chainyA2CmF">`SuggestionType.chain`</a> or <a href="sdk-for-ios-navigate-enums-suggestiontype#/s:7heresdk14SuggestionTypeO8categoryyA2CmF">`SuggestionType.category`</a>

With “Place” you get data for a concrete place in the world. With “Query” something to follow-up, a way to perform more focused search.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk10SuggestionC5titleSSvp"></span>` `<span id="//apple_ref/swift/Property/title" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-suggestion#/s:7heresdk10SuggestionC5titleSSvp" class="token"><code>title</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The localized title for the suggestion.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var title: String { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SuggestionC4typeAA0B4TypeOvp"></span>` `<span id="//apple_ref/swift/Property/type" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-suggestion#/s:7heresdk10SuggestionC4typeAA0B4TypeOvp" class="token"><code>type</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Type of the suggestion.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var type: SuggestionType { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SuggestionC5placeAA5PlaceCSgvp"></span>` `<span id="//apple_ref/swift/Property/place" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-suggestion#/s:7heresdk10SuggestionC5placeAA5PlaceCSgvp" class="token"><code>place</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The suggested place. Available only for <a href="sdk-for-ios-navigate-enums-suggestiontype#/s:7heresdk14SuggestionTypeO5placeyA2CmF">`SuggestionType.place`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var place: Place? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SuggestionC2idSSSgvp"></span>` `<span id="//apple_ref/swift/Property/id" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-suggestion#/s:7heresdk10SuggestionC2idSSSgvp" class="token"><code>id</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The unique id of suggested item. It can be used to query further information. For online search, suggestion of type <a href="sdk-for-ios-navigate-enums-suggestiontype#/s:7heresdk14SuggestionTypeO5placeyA2CmF">`SuggestionType.place`</a> will have Suggestion.id same as Place.id. For offline search, only suggestion of type <a href="sdk-for-ios-navigate-enums-suggestiontype#/s:7heresdk14SuggestionTypeO5chainyA2CmF">`SuggestionType.chain`</a>, will have this property filled with identifier number of an associated chain. For example, the chain ID “8778” corresponds to the chain name “ABC Shop”. For other types, <a href="sdk-for-ios-navigate-enums-suggestiontype#/s:7heresdk14SuggestionTypeO5placeyA2CmF">`SuggestionType.place`</a> and <a href="sdk-for-ios-navigate-enums-suggestiontype#/s:7heresdk14SuggestionTypeO8categoryyA2CmF">`SuggestionType.category`</a> this property will be null.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var id: String? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10SuggestionC4hrefSSSgvp"></span>` `<span id="//apple_ref/swift/Property/href" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-suggestion#/s:7heresdk10SuggestionC4hrefSSSgvp" class="token"><code>href</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Direct URL for precise query. Available only for <a href="sdk-for-ios-navigate-enums-suggestiontype#/s:7heresdk14SuggestionTypeO5chainyA2CmF">`SuggestionType.chain`</a> and <a href="sdk-for-ios-navigate-enums-suggestiontype#/s:7heresdk14SuggestionTypeO8categoryyA2CmF">`SuggestionType.category`</a>. This is not supported in offline search.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var href: String? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      getHighlights()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The text slices matching the input query.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getHighlights () -> [ HighlightType : [ IndexRange ]]
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  Associated container where <a href="sdk-for-ios-navigate-enums-highlighttype">`HighlightType`</a> is a key and list of <a href="sdk-for-ios-navigate-classes-indexrange">`IndexRange`</a> value.

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

