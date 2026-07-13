---
title: "setProfile method - SpeedBasedCameraBehavior class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-speedbasedcamerabehavior-setprofile"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setProfile.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/SpeedBasedCameraBehavior-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setProfile</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setProfile</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setProfile-param-profile" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-speedbasedcamerabehaviorprofilevalue-class">SpeedBasedCameraBehaviorProfileValue</a></span>\></span></span> <span class="parameter-name">profile</span></span>

)

</div>

<div class="section desc markdown">

Sets the profile.

The speed ranges within the profile can overlap in order to prevent oscillations between adjacent levels. Provided profile must satisfy following conditions:

- profile must not be empty

- each speed range must be valid (fromMetersPerSecond must be less then toMetersPerSecond)

- ranges must be sorted by fromMetersPerSecond and toMetersPerSecond

- gaps between ranges are not allowed Invalid profile will be rejected and error message logged with explanation of violated restriction.

- `profile` The new profile value.

</div>

## Implementation

``` dart
void setProfile(List<SpeedBasedCameraBehaviorProfileValue> profile);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
