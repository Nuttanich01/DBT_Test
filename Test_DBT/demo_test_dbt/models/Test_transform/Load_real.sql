with real_data as (
    select * from {{ref ('transform_all_data')}}
)

 select * from real_data