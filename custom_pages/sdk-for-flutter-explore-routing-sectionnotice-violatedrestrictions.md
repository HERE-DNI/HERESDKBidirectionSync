---
title: "violatedRestrictions property - SectionNotice class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-sectionnotice-violatedrestrictions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- violatedRestrictions.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/SectionNotice-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">violatedRestrictions</span> property

</div>

<div class="section multi-line-signature">

List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-routing-violatedrestriction-class">ViolatedRestriction</a></span>\></span> <span class="name">violatedRestrictions</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The following property `violated_restrictions` contains the notice detail information. Only three types of restrictions can have notice details: time dependent restriction, vehicle restriction and transport mode restriction. There is no one-to-one match of the `SectionNotice.code` and these three restriction types. For example, if `SectionNotice.code` is <a href="sdk-for-flutter-explore-routing-sectionnoticecode">SectionNoticeCode.violatedVehicleRestriction</a>, then it can be either vehicle restriction or transport mode restriction. If `SectionNotice.code` is <a href="sdk-for-flutter-explore-routing-sectionnoticecode">SectionNoticeCode.seasonalClosure</a>, then it is time dependent restriction. If the section notice is none of the above-mentioned three types, then this will be an empty list.

</div>

## Implementation

``` dart
List<ViolatedRestriction> violatedRestrictions;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
