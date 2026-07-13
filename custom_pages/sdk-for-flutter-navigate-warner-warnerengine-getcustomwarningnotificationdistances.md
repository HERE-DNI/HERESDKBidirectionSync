---
title: "getCustomWarningNotificationDistances method - WarnerEngine class - warner library - Dart API"
slug: "sdk-for-flutter-navigate-warner-warnerengine-getcustomwarningnotificationdistances"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getCustomWarningNotificationDistances.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="warner/WarnerEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">getCustomWarningNotificationDistances</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a></span> <span class="name">getCustomWarningNotificationDistances</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-getCustomWarningNotificationDistances-param-customWarningType" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">customWarningType</span></span>

)

</div>

<div class="section desc markdown">

Returns the warning notification distances for the specified custom warning type.

Unlike <a href="sdk-for-flutter-navigate-warner-warnerengine-getwarningnotificationdistances">WarnerEngine.getWarningNotificationDistances</a>, which operates on a <a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a>, this method targets a specific custom warning category identified by `WarnerEngine.getCustomWarningNotificationDistances.customWarningType`, as defined in <a href="sdk-for-flutter-navigate-warner-customwarning-customwarningtype">CustomWarning.customWarningType</a> and <a href="sdk-for-flutter-navigate-warner-warning-customwarningtype">Warning.customWarningType</a>.

- `customWarningType` The identifier of the custom warning type for which the notification distances are requested.

Returns <a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a>. The warning notification distances configured for the given `WarnerEngine.getCustomWarningNotificationDistances.customWarningType`. If no distances have been explicitly set for this type, a default <a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a> value is returned.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
WarningNotificationDistances getCustomWarningNotificationDistances(int customWarningType);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
