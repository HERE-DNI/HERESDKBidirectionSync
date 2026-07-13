---
title: "id property - Suggestion class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-suggestion-id"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/Suggestion-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">id</span> property

</div>

<div id="sdk-for-flutter-explore-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">String?</span> <span class="name">id</span>

</div>

<div class="section desc markdown">

The unique id of suggested item. It can be used to query further information. For online search, suggestion of type <a href="sdk-for-flutter-explore-search-suggestiontype">SuggestionType.place</a> will have Suggestion.id same as Place.id. For offline search, only suggestion of type <a href="sdk-for-flutter-explore-search-suggestiontype">SuggestionType.chain</a>, will have this property filled with identifier number of an associated chain. For example, the chain ID "8778" corresponds to the chain name "ABC Shop". For other types, <a href="sdk-for-flutter-explore-search-suggestiontype">SuggestionType.place</a> and <a href="sdk-for-flutter-explore-search-suggestiontype">SuggestionType.category</a> this property will be null. Gets the suggested item id.

</div>

## Implementation

``` dart
String? get id;
```

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

