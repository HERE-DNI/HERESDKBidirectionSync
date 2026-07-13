---
title: "secondaryLanguage property - HereMapController class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-heremapcontroller-secondarylanguage"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/HereMapController-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">secondaryLanguage</span> property

</div>

<div id="sdk-for-flutter-explore-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-languagecode">LanguageCode</a>?</span> <span class="name">secondaryLanguage</span>

</div>

<div class="section desc markdown">

The code of desired secondary map display language. Note: This feature is in beta state and thus there can be bugs and unexpected behavior.

</div>

## Implementation

``` dart
static LanguageCode? get secondaryLanguage => $prototype.secondaryLanguage;
```

</div>

<div id="sdk-for-flutter-explore-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">secondaryLanguage=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-secondaryLanguage-param-languageCode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-languagecode">LanguageCode</a>?</span> <span class="parameter-name">languageCode</span></span>)</span>

</div>

<div class="section desc markdown">

Sets the desired secondary map display language for all instances of MapView to `languageCode`. Applying a language change causes map to be redrawn. If the specified language is not supported, local language of the region will be used. If null, no secondary map language will be used which is the default behaviour. Note: This feature is in beta state and thus there can be bugs and unexpected behavior.

</div>

## Implementation

``` dart
static void set secondaryLanguage(LanguageCode? languageCode) {
  $prototype.secondaryLanguage = languageCode;
}
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

