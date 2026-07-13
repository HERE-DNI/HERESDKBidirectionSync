---
title: "enablePhoneme property - ManeuverNotificationOptions class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-enablephoneme"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- enablePhoneme.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/ManeuverNotificationOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">enablePhoneme</span> property

</div>

<div class="section multi-line-signature">

bool <span class="name">enablePhoneme</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

A flag that indicates whether phonemes in selected notification format for proper nouns (e.g. road names, road numbers, city names) should be used when generating notifications. Direction information comes usually in orthographic form and phoneme (e.g. Wall Street and "wɔːl"striːt). However, when the notification is synthesized by a TTS engine, the pronunciation of the orthographic form solely depends on its capability and phoneme set. The use of our phoneme data in the notification usually makes the pronunciation of direction information sound more natural. **Note:** For now, this property is functional for road name and road number information only.

Defaults to `false`.

</div>

## Implementation

``` dart
bool enablePhoneme;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
