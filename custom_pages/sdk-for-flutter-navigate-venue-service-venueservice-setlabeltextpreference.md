---
title: "setLabeltextPreference method - VenueService class - venue.service library - Dart API"
slug: "sdk-for-flutter-navigate-venue-service-venueservice-setlabeltextpreference"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.service/VenueService-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setLabeltextPreference</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setLabeltextPreference</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setLabeltextPreference-param-labelTextPref" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span> <span class="parameter-name">labelTextPref</span></span>

)

</div>

<div class="section desc markdown">

Sets override labelTextPreference for labels.

- `labelTextPref` The list of string override labelTextPreference.

"OCCUPANT_NAMES" - To display only occupant names on map as a label text. Example: Boutique Du Chocolat for id 7348

"SPACE_NAME" - To display only space names on map as a label text. Example: Family Services/First Aid for id 7348

"SPACE_TYPE_NAME" - To display only space types on map as a label text. Example: DEFIBRILLATOR for id 7348

"SPACE_CATEGORY_NAME" - To display only space categories on map as a label text. Example: SAFETY for id 7348

"INTERNAL_ADDRESS" - To display only internal addresses on map as a label text. Example: 51/D for id 7348

</div>

## Implementation

``` dart
void setLabeltextPreference(List<String> labelTextPref);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

