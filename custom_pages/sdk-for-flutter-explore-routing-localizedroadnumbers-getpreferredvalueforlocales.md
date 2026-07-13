---
title: "getPreferredValueForLocales method - LocalizedRoadNumbers class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-localizedroadnumbers-getpreferredvalueforlocales"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/LocalizedRoadNumbers-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getPreferredValueForLocales</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype">String?</span> <span class="name">getPreferredValueForLocales</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-getPreferredValueForLocales-param-locales" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="https://pub.dev/documentation/intl/0.20.2/locale/Locale-class.html">Locale</a></span>\></span></span> <span class="parameter-name">locales</span></span>

)

</div>

<div class="section desc markdown">

Returns best name or title to be presented to the user according to specified locales.

The locales are expected to be ordered by priority. If no matching locale found - the default is returned. In case of empty list returns `null`.

- `locales` Locales

Returns `String?`. The best name or title to be presented to the user according to specified locales, default or `null` if list is empty.

</div>

## Implementation

``` dart
String? getPreferredValueForLocales(List<Locale> locales) => $prototype.getPreferredValueForLocales(this, locales);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

