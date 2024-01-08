
with final as (
    
    select * from {{ref ('raw1')}}
    UNION ALL
    select * from {{ref ('raw3')}}
    UNION ALL
    select * from {{ref ('raw4')}}
    UNION ALL
    select * from {{ref ('raw2')}}

)

select * from final