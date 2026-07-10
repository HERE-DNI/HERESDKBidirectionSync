---
title: "EventTextListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-eventtextlistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">EventTextListener</span>

</div>

<div class="block">

This interface should be implemented in order to receive notifications when text notifications are available from Navigator . Multiple notifications can be given for the same maneuver at different distances.

</div>

</div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onEventTextUpdated ( EventText eventText)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called whenever there is a new text notification for a maneuver (multiple notifications can be given for the same maneuver at different distances (for example: "After 500 meters turn right." or "Now turn right.") and in that case, this method will be called once for each distance.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onEventTextUpdated-com-here-sdk-navigation-EventText" class="section detail">

    ### onEventTextUpdated

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onEventTextUpdated</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtext" title="class in com.here.sdk.navigation">EventText</a> eventText)</span>

    </div>

    <div class="block">

    Called whenever there is a new text notification for a maneuver (multiple notifications can be given for the same maneuver at different distances (for example: "After 500 meters turn right." or "Now turn right.") and in that case, this method will be called once for each distance.

    </div>

    Parameters:  
    `eventText` -

    Data related to next text announcement.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

