---
title: "SegmentReference (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestsegmentreference"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class SegmentReference

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.SegmentReference
------------------------------------------------------------------------
public final class SegmentReference extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Reference to a segment id with a travel direction.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html)

  [localId](#localId)

Local ID of the segment inside the OCM tile.

`double`

  [offsetEnd](#offsetEnd)

The end offset is a non-negative number between 0 and 1, representing the end of the referenced range using a proportion of the length of the segment.

`double`

  [offsetStart](#offsetStart)

The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [segmentId](#segmentId)

Topology segment id representing a unique identifier within the HERE platform catalogs.

`long`

  [tilePartitionId](#tilePartitionId)

HERE tile partition id (Morton-encoding + level indicator) of the segment.

[`TravelDirection`](sdk-for-android-explore-api-reference-latesttraveldirection "enum class in com.here.sdk.routing")

  [travelDirection](#travelDirection)

Travel direction of the segment.

## Constructor Summary

Constructors

Constructor

  Description

  [SegmentReference](#%3Cinit%3E())`()`

Creates a new instance.

[SegmentReference](#%3Cinit%3E(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` segmentId)`

Creates a new instance.

[SegmentReference](#%3Cinit%3E(java.lang.String,com.here.sdk.routing.TravelDirection))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` segmentId, `[`TravelDirection`](sdk-for-android-explore-api-reference-latesttraveldirection "enum class in com.here.sdk.routing")` travelDirection)`

Creates a new instance.

[SegmentReference](#%3Cinit%3E(java.lang.String,com.here.sdk.routing.TravelDirection,double))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` segmentId, `[`TravelDirection`](sdk-for-android-explore-api-reference-latesttraveldirection "enum class in com.here.sdk.routing")` travelDirection, double offsetStart)`

Creates a new instance.

[SegmentReference](#%3Cinit%3E(java.lang.String,com.here.sdk.routing.TravelDirection,double,double))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` segmentId, `[`TravelDirection`](sdk-for-android-explore-api-reference-latesttraveldirection "enum class in com.here.sdk.routing")` travelDirection, double offsetStart, double offsetEnd)`

Creates a new instance.

[SegmentReference](#%3Cinit%3E(java.lang.String,com.here.sdk.routing.TravelDirection,double,double,long))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` segmentId, `[`TravelDirection`](sdk-for-android-explore-api-reference-latesttraveldirection "enum class in com.here.sdk.routing")` travelDirection, double offsetStart, double offsetEnd, long tilePartitionId)`

Creates a new instance.

[SegmentReference](#%3Cinit%3E(java.lang.String,com.here.sdk.routing.TravelDirection,double,double,long,java.lang.Long))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` segmentId, `[`TravelDirection`](sdk-for-android-explore-api-reference-latesttraveldirection "enum class in com.here.sdk.routing")` travelDirection, double offsetStart, double offsetEnd, long tilePartitionId, `[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html)` localId)`

Creates a new instance.

## Method Summary

  All Methods
  Static Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  `static `[`SegmentReference`](sdk-for-android-explore-api-reference-latestsegmentreference "class in com.here.sdk.routing")

  [fromString](#fromString(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` segmentRef)`

Returns an instance of this struct from a string if it's well-formatted, `null` otherwise.

`int`

  [hashCode](#hashCode())`()`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### segmentId

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) segmentId

    Topology segment id representing a unique identifier within the HERE platform catalogs.

### travelDirection

@NonNull public [TravelDirection](sdk-for-android-explore-api-reference-latesttraveldirection "enum class in com.here.sdk.routing") travelDirection

    Travel direction of the segment.

### offsetStart

public double offsetStart

    The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)

### offsetEnd

public double offsetEnd

    The end offset is a non-negative number between 0 and 1, representing the end of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)

### tilePartitionId

public long tilePartitionId

    HERE tile partition id (Morton-encoding + level indicator) of the segment. As in HERE Map Content.

### localId

@Nullable public [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html) localId

    Local ID of the segment inside the OCM tile.

## Constructor Details

  - ()" class="section detail">

### SegmentReference

public SegmentReference()

    Creates a new instance.

  - (java.lang.String)" class="section detail">

### SegmentReference

public SegmentReference(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) segmentId)

    Creates a new instance.
Parameters:
    `segmentId` -

    Topology segment id representing a unique identifier within the HERE platform catalogs.
- (java.lang.String,com.here.sdk.routing.TravelDirection)" class="section detail">

### SegmentReference

public SegmentReference(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) segmentId, @NonNull [TravelDirection](sdk-for-android-explore-api-reference-latesttraveldirection "enum class in com.here.sdk.routing") travelDirection)

    Creates a new instance.
Parameters:
    `segmentId` -

    Topology segment id representing a unique identifier within the HERE platform catalogs.

    `travelDirection` -

    Travel direction of the segment.
- (java.lang.String,com.here.sdk.routing.TravelDirection,double)" class="section detail">

### SegmentReference

public SegmentReference(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) segmentId, @NonNull [TravelDirection](sdk-for-android-explore-api-reference-latesttraveldirection "enum class in com.here.sdk.routing") travelDirection, double offsetStart)

    Creates a new instance.
Parameters:
    `segmentId` -

    Topology segment id representing a unique identifier within the HERE platform catalogs.

    `travelDirection` -

    Travel direction of the segment.

    `offsetStart` -

    The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)
- (java.lang.String,com.here.sdk.routing.TravelDirection,double,double)" class="section detail">

### SegmentReference

public SegmentReference(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) segmentId, @NonNull [TravelDirection](sdk-for-android-explore-api-reference-latesttraveldirection "enum class in com.here.sdk.routing") travelDirection, double offsetStart, double offsetEnd)

    Creates a new instance.
Parameters:
    `segmentId` -

    Topology segment id representing a unique identifier within the HERE platform catalogs.

    `travelDirection` -

    Travel direction of the segment.

    `offsetStart` -

    The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)

    `offsetEnd` -

    The end offset is a non-negative number between 0 and 1, representing the end of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)
- (java.lang.String,com.here.sdk.routing.TravelDirection,double,double,long)" class="section detail">

### SegmentReference

public SegmentReference(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) segmentId, @NonNull [TravelDirection](sdk-for-android-explore-api-reference-latesttraveldirection "enum class in com.here.sdk.routing") travelDirection, double offsetStart, double offsetEnd, long tilePartitionId)

    Creates a new instance.
Parameters:
    `segmentId` -

    Topology segment id representing a unique identifier within the HERE platform catalogs.

    `travelDirection` -

    Travel direction of the segment.

    `offsetStart` -

    The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)

    `offsetEnd` -

    The end offset is a non-negative number between 0 and 1, representing the end of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)

    `tilePartitionId` -

    HERE tile partition id (Morton-encoding + level indicator) of the segment. As in HERE Map Content.
- (java.lang.String,com.here.sdk.routing.TravelDirection,double,double,long,java.lang.Long)" class="section detail">

### SegmentReference

public SegmentReference(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) segmentId, @NonNull [TravelDirection](sdk-for-android-explore-api-reference-latesttraveldirection "enum class in com.here.sdk.routing") travelDirection, double offsetStart, double offsetEnd, long tilePartitionId, @Nullable [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html) localId)

    Creates a new instance.
Parameters:
    `segmentId` -

    Topology segment id representing a unique identifier within the HERE platform catalogs.

    `travelDirection` -

    Travel direction of the segment.

    `offsetStart` -

    The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)

    `offsetEnd` -

    The end offset is a non-negative number between 0 and 1, representing the end of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)

    `tilePartitionId` -

    HERE tile partition id (Morton-encoding + level indicator) of the segment. As in HERE Map Content.

    `localId` -

    Local ID of the segment inside the OCM tile.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### fromString

@Nullable public static [SegmentReference](sdk-for-android-explore-api-reference-latestsegmentreference "class in com.here.sdk.routing") fromString(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) segmentRef)

    Returns an instance of this struct from a string if it's well-formatted, `null` otherwise.
Parameters:
    `segmentRef` -

    The string to parse

    Returns:
    An instance of [`SegmentReference`](sdk-for-android-explore-api-reference-latestsegmentreference "class in com.here.sdk.routing") from a string if it's well-formatted, `null` otherwise.
