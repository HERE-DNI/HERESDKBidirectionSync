---
title: "LocationIssueListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-location-locationissuelistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-location-package-summary">com.here.sdk.location</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">LocationIssueListener</span>

</div>

<div class="block">

interface receiving notifications when the set of currently active location issues changes. Location issues represent unexpected or degraded conditions affecting positioning quality, availability, or functionality. The LocationEngine monitors various positioning subsystems and aggregates detected issues into a unified snapshot delivered via this interface. Each callback delivers the complete current set of active issues. An empty list indicates all previously reported issues have cleared. Issues are transient by design and automatically removed once underlying conditions improve. No explicit clear/dismiss API is provided.

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

      onLocationIssueChanged ( List < LocationIssueType > issues)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called when the snapshot of currently active location issues changes.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onLocationIssueChanged-java-util-List" class="section detail">

    ### onLocationIssueChanged

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onLocationIssueChanged</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a>\> issues)</span>

    </div>

    <div class="block">

    Called when the snapshot of currently active location issues changes. Invoked whenever the LocationEngine detects a change in the set of active issues, including when all issues clear (empty list). Replace any previously stored issue list with this snapshot.

    </div>

    Parameters:  
    `issues` -

    Current snapshot of active location issues. Empty list indicates no active issues.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

